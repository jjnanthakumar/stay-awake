"""Core Stay Awake functionality."""

import time
import signal
import logging
from datetime import datetime
from typing import Optional

from config import Config
from modes import create_mode, ActivityMode


class StayAwake:
    """Main Stay Awake application."""
    
    def __init__(self, config: Optional[Config] = None):
        """Initialize Stay Awake with configuration."""
        self.config = config or Config()
        self.running = False
        self.activity_mode: Optional[ActivityMode] = None
        self.logger = self._setup_logging()
        self._setup_signal_handlers()
        self.activity_count = 0
        self.start_time: Optional[datetime] = None
    
    def _setup_logging(self) -> logging.Logger:
        """Set up logging configuration."""
        logger = logging.getLogger('stay_awake')
        logger.setLevel(getattr(logging, self.config.log_level))
        
        # Clear existing handlers
        logger.handlers.clear()
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, self.config.log_level))
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File handler (if configured)
        if self.config.log_file:
            file_handler = logging.FileHandler(self.config.log_file)
            file_handler.setLevel(getattr(logging, self.config.log_level))
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger
    
    def _setup_signal_handlers(self) -> None:
        """Set up signal handlers for graceful shutdown."""
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame) -> None:
        """Handle shutdown signals."""
        self.logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.stop()
    
    def start(self) -> None:
        """Start the Stay Awake service."""
        # Validate configuration
        errors = self.config.validate()
        if errors:
            self.logger.error("Configuration errors:")
            for error in errors:
                self.logger.error(f"  - {error}")
            raise ValueError("Invalid configuration")
        
        self.activity_mode = create_mode(self.config)
        self.running = True
        self.start_time = datetime.now()
        self.activity_count = 0
        
        self.logger.info("=" * 60)
        self.logger.info("Stay Awake Service Started")
        self.logger.info("=" * 60)
        self.logger.info(f"Mode: {self.config.mode}")
        self.logger.info(f"Activity: {self.activity_mode.get_description()}")
        self.logger.info(f"Interval: {self.config.interval} seconds")
        self.logger.info(f"Press Ctrl+C to stop")
        self.logger.info("=" * 60)
        
        self._run_loop()
    
    def _run_loop(self) -> None:
        """Main execution loop."""
        try:
            while self.running:
                self._perform_activity()
                if self.running:  # Check again in case stopped during activity
                    time.sleep(self.config.interval)
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}", exc_info=True)
            self.stop()
    
    def _perform_activity(self) -> None:
        """Perform a single activity cycle."""
        try:
            self.activity_count += 1
            self.logger.debug(f"Performing activity #{self.activity_count}")
            
            start = time.time()
            self.activity_mode.execute()
            elapsed = time.time() - start
            
            self.logger.info(
                f"Activity #{self.activity_count} completed in {elapsed:.2f}s "
                f"({self.activity_mode.get_description()})"
            )
        except Exception as e:
            self.logger.error(f"Error performing activity: {e}", exc_info=True)
    
    def stop(self) -> None:
        """Stop the Stay Awake service."""
        if not self.running:
            return
        
        self.running = False
        
        # Calculate statistics
        if self.start_time:
            duration = datetime.now() - self.start_time
            hours, remainder = divmod(duration.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            
            self.logger.info("=" * 60)
            self.logger.info("Stay Awake Service Stopped")
            self.logger.info("=" * 60)
            self.logger.info(f"Total activities performed: {self.activity_count}")
            self.logger.info(f"Total runtime: {int(hours)}h {int(minutes)}m {int(seconds)}s")
            self.logger.info("=" * 60)
    
    def get_status(self) -> dict:
        """Get current status information."""
        uptime = None
        if self.start_time:
            uptime = (datetime.now() - self.start_time).total_seconds()
        
        return {
            "running": self.running,
            "mode": self.config.mode,
            "interval": self.config.interval,
            "activity_count": self.activity_count,
            "uptime_seconds": uptime,
            "start_time": self.start_time.isoformat() if self.start_time else None
        }
