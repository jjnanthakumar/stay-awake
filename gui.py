"""
Graphical User Interface for NJStayAwake.
Provides an easy-to-use interface for all NJStayAwake features.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import threading
from pathlib import Path
from datetime import datetime, timedelta

from config import Config
from core import StayAwake


class StayAwakeGUI:
    """GUI application for NJStayAwake."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("NJStayAwake - Prevent Sleep")
        self.root.geometry("600x750")
        self.root.resizable(True, True)
        
        # Set window icon
        try:
            logo_path = Path(__file__).parent / "logo.png"
            if logo_path.exists():
                icon = tk.PhotoImage(file=str(logo_path))
                self.root.iconphoto(True, icon)
        except Exception as e:
            pass  # Fallback to default icon if logo not found
        
        # App state
        self.stay_awake = None
        self.running = False
        self.config = Config()
        self.start_time = None
        self.update_job = None
        
        # Try to load existing config
        default_config_path = Config.get_default_config_path()
        if default_config_path.exists():
            self.config = Config.load(default_config_path)
        
        # Setup UI
        self._setup_ui()
        self._load_config_to_ui()
        self._update_status()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _setup_ui(self):
        """Create the user interface."""
        # Title
        title_frame = ttk.Frame(self.root, padding="8")
        title_frame.pack(fill=tk.X)
        
        ttk.Label(
            title_frame,
            text="NJStayAwake",
            font=("Arial", 18, "bold")
        ).pack()
        
        ttk.Label(
            title_frame,
            text="Keep your computer active",
            font=("Arial", 9)
        ).pack()
        
        # Main content frame
        main_frame = ttk.Frame(self.root, padding="8")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status Section
        self._create_status_section(main_frame)
        
        # Mode Section
        self._create_mode_section(main_frame)
        
        # Timing Section
        self._create_timing_section(main_frame)
        
        # Mouse Settings Section
        self._create_mouse_section(main_frame)
        
        # Keyboard Settings Section
        self._create_keyboard_section(main_frame)
        
        # Logging Section
        self._create_logging_section(main_frame)
        
        # Control Buttons
        self._create_control_buttons(main_frame)
        
        # Footer
        self._create_footer()
    
    def _create_status_section(self, parent):
        """Create status display section."""
        frame = ttk.LabelFrame(parent, text="Status", padding="6")
        frame.pack(fill=tk.X, pady=2)
        
        self.status_label = ttk.Label(
            frame,
            text="● Stopped",
            font=("Arial", 12, "bold"),
            foreground="red"
        )
        self.status_label.pack()
        
        self.stats_label = ttk.Label(
            frame,
            text="Ready to start",
            font=("Arial", 9)
        )
        self.stats_label.pack()
    
    def _create_mode_section(self, parent):
        """Create activity mode selection."""
        frame = ttk.LabelFrame(parent, text="Activity Mode", padding="6")
        frame.pack(fill=tk.X, pady=2)
        
        self.mode_var = tk.StringVar(value="minimal")
        
        modes = [
            ("Minimal", "minimal"),
            ("Mouse", "mouse"),
            ("Keyboard", "keyboard"),
            ("Full", "full")
        ]
        
        for text, value in modes:
            ttk.Radiobutton(
                frame,
                text=text,
                variable=self.mode_var,
                value=value,
                command=self._on_mode_change
            ).pack(anchor=tk.W, pady=1)
    
    def _create_timing_section(self, parent):
        """Create timing configuration."""
        frame = ttk.LabelFrame(parent, text="Timing", padding="6")
        frame.pack(fill=tk.X, pady=2)
        
        # Interval
        interval_frame = ttk.Frame(frame)
        interval_frame.pack(fill=tk.X, pady=1)
        
        ttk.Label(interval_frame, text="Interval (sec):").pack(side=tk.LEFT)
        self.interval_var = tk.IntVar(value=60)
        interval_spinbox = ttk.Spinbox(
            interval_frame,
            from_=10,
            to=600,
            textvariable=self.interval_var,
            width=10
        )
        interval_spinbox.pack(side=tk.RIGHT)
        
        # Duration
        duration_frame = ttk.Frame(frame)
        duration_frame.pack(fill=tk.X, pady=1)
        
        ttk.Label(duration_frame, text="Duration (sec):").pack(side=tk.LEFT)
        self.duration_var = tk.DoubleVar(value=0.5)
        duration_spinbox = ttk.Spinbox(
            duration_frame,
            from_=0.1,
            to=5.0,
            increment=0.1,
            textvariable=self.duration_var,
            width=10
        )
        duration_spinbox.pack(side=tk.RIGHT)
    
    def _create_mouse_section(self, parent):
        """Create mouse settings."""
        frame = ttk.LabelFrame(parent, text="Mouse Settings", padding="6")
        frame.pack(fill=tk.X, pady=2)
        
        # Pattern
        pattern_frame = ttk.Frame(frame)
        pattern_frame.pack(fill=tk.X, pady=1)
        
        ttk.Label(pattern_frame, text="Pattern:").pack(side=tk.LEFT)
        self.pattern_var = tk.StringVar(value="linear")
        pattern_combo = ttk.Combobox(
            pattern_frame,
            textvariable=self.pattern_var,
            values=["linear", "circle", "random"],
            state="readonly",
            width=12
        )
        pattern_combo.pack(side=tk.RIGHT)
        
        # Distance
        distance_frame = ttk.Frame(frame)
        distance_frame.pack(fill=tk.X, pady=1)
        
        ttk.Label(distance_frame, text="Distance (px):").pack(side=tk.LEFT)
        self.distance_var = tk.IntVar(value=50)
        distance_spinbox = ttk.Spinbox(
            distance_frame,
            from_=10,
            to=200,
            textvariable=self.distance_var,
            width=10
        )
        distance_spinbox.pack(side=tk.RIGHT)
    
    def _create_keyboard_section(self, parent):
        """Create keyboard settings."""
        frame = ttk.LabelFrame(parent, text="Keyboard Settings", padding="6")
        frame.pack(fill=tk.X, pady=2)
        
        # Key - Dropdown for user-friendliness
        key_frame = ttk.Frame(frame)
        key_frame.pack(fill=tk.X, pady=1)
        
        ttk.Label(key_frame, text="Key:").pack(side=tk.LEFT)
        self.key_var = tk.StringVar(value="shift")
        key_combo = ttk.Combobox(
            key_frame,
            textvariable=self.key_var,
            values=["shift", "ctrl", "alt", "f13", "f14", "f15", "scrolllock", "numlock"],
            state="readonly",
            width=12
        )
        key_combo.pack(side=tk.RIGHT)
        
        # Presses
        presses_frame = ttk.Frame(frame)
        presses_frame.pack(fill=tk.X, pady=1)
        
        ttk.Label(presses_frame, text="Presses:").pack(side=tk.LEFT)
        self.presses_var = tk.IntVar(value=1)
        presses_spinbox = ttk.Spinbox(
            presses_frame,
            from_=1,
            to=10,
            textvariable=self.presses_var,
            width=10
        )
        presses_spinbox.pack(side=tk.RIGHT)
    
    def _create_logging_section(self, parent):
        """Create logging settings."""
        frame = ttk.LabelFrame(parent, text="Logging", padding="6")
        frame.pack(fill=tk.X, pady=2)
        
        # Log level
        level_frame = ttk.Frame(frame)
        level_frame.pack(fill=tk.X, pady=1)
        
        ttk.Label(level_frame, text="Level:").pack(side=tk.LEFT)
        self.log_level_var = tk.StringVar(value="INFO")
        level_combo = ttk.Combobox(
            level_frame,
            textvariable=self.log_level_var,
            values=["DEBUG", "INFO", "WARNING", "ERROR"],
            state="readonly",
            width=12
        )
        level_combo.pack(side=tk.RIGHT)
    
    def _create_control_buttons(self, parent):
        """Create start/stop and configuration buttons."""
        # Main controls
        control_frame = ttk.Frame(parent, padding="3")
        control_frame.pack(fill=tk.X, pady=5)
        
        button_container = ttk.Frame(control_frame)
        button_container.pack(expand=True)
        
        self.start_button = ttk.Button(
            button_container,
            text="▶ Start",
            command=self._start_service,
            width=20
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(
            button_container,
            text="■ Stop",
            command=self._stop_service,
            state=tk.DISABLED,
            width=20
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Config buttons
        config_frame = ttk.Frame(parent, padding="3")
        config_frame.pack(fill=tk.X, pady=3)
        
        config_container = ttk.Frame(config_frame)
        config_container.pack(expand=True)
        
        ttk.Button(
            config_container,
            text="Load Config",
            command=self._load_config,
            width=20
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            config_container,
            text="Save Config",
            command=self._save_config,
            width=20
        ).pack(side=tk.LEFT, padx=5)
    
    def _create_footer(self):
        """Create footer with info."""
        footer = ttk.Frame(self.root, padding="5")
        footer.pack(side=tk.BOTTOM, fill=tk.X)
        
        ttk.Label(
            footer,
            text="NJStayAwake v1.0.0 | Press Stop or close window to exit",
            font=("Arial", 8),
            foreground="gray"
        ).pack()
    
    def _on_mode_change(self):
        """Handle mode change."""
        # Could enable/disable relevant sections based on mode
        pass
    
    def _load_config_to_ui(self):
        """Load configuration values into UI."""
        self.mode_var.set(self.config.mode)
        self.interval_var.set(self.config.interval)
        self.duration_var.set(self.config.duration)
        self.pattern_var.set(self.config.mouse_pattern)
        self.distance_var.set(self.config.mouse_distance)
        self.key_var.set(self.config.keyboard_key)
        self.presses_var.set(self.config.keyboard_presses)
        self.log_level_var.set(self.config.log_level)
    
    def _ui_to_config(self):
        """Update config from UI values."""
        self.config.mode = self.mode_var.get()
        self.config.interval = self.interval_var.get()
        self.config.duration = self.duration_var.get()
        self.config.mouse_pattern = self.pattern_var.get()
        self.config.mouse_distance = self.distance_var.get()
        self.config.keyboard_key = self.key_var.get()
        self.config.keyboard_presses = self.presses_var.get()
        self.config.log_level = self.log_level_var.get()
    
    def _start_service(self):
        """Start the Stay Awake service."""
        # Update config from UI
        self._ui_to_config()
        
        # Validate
        errors = self.config.validate()
        if errors:
            messagebox.showerror(
                "Configuration Error",
                "Invalid configuration:\n" + "\n".join(errors)
            )
            return
        
        # Create and start service in thread
        self.stay_awake = StayAwake(self.config)
        self.running = True
        self.start_time = datetime.now()
        
        # Start in background thread
        thread = threading.Thread(target=self._run_service, daemon=True)
        thread.start()
        
        # Update UI
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self._update_status()
    
    def _run_service(self):
        """Run the service (called in background thread)."""
        try:
            self.stay_awake.start()
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
            self.running = False
            self.root.after(0, self._update_status)
    
    def _stop_service(self):
        """Stop the Stay Awake service."""
        if self.stay_awake:
            self.stay_awake.stop()
        
        self.running = False
        
        # Update UI
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self._update_status()
        
        # Show summary
        if self.start_time and self.stay_awake:
            stats = self.stay_awake.get_status()
            duration = datetime.now() - self.start_time
            hours, remainder = divmod(duration.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            
            messagebox.showinfo(
                "Service Stopped",
                f"Stay Awake has stopped.\n\n"
                f"Activities performed: {stats['activity_count']}\n"
                f"Total runtime: {int(hours)}h {int(minutes)}m {int(seconds)}s"
            )
        
        self.start_time = None
    
    def _update_status(self):
        """Update status display."""
        if self.running and self.stay_awake:
            stats = self.stay_awake.get_status()
            self.status_label.config(text="● Running", foreground="green")
            
            # Calculate uptime
            if self.start_time:
                uptime = datetime.now() - self.start_time
                hours, remainder = divmod(uptime.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                
                self.stats_label.config(
                    text=f"Activities: {stats['activity_count']} | "
                         f"Uptime: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d} | "
                         f"Mode: {stats['mode']}"
                )
            
            # Schedule next update
            self.update_job = self.root.after(1000, self._update_status)
        else:
            self.status_label.config(text="● Stopped", foreground="red")
            self.stats_label.config(text="Ready to start")
            
            if self.update_job:
                self.root.after_cancel(self.update_job)
                self.update_job = None
    
    def _load_config(self):
        """Load configuration from file."""
        filename = filedialog.askopenfilename(
            title="Load Configuration",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            defaultextension=".json"
        )
        
        if filename:
            try:
                self.config = Config.load(Path(filename))
                self._load_config_to_ui()
                messagebox.showinfo("Success", "Configuration loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load config:\n{e}")
    
    def _save_config(self):
        """Save configuration to file."""
        filename = filedialog.asksaveasfilename(
            title="Save Configuration",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            defaultextension=".json",
            initialfile="njstayawake-config.json"
        )
        
        if filename:
            try:
                self._ui_to_config()
                self.config.save(Path(filename))
                messagebox.showinfo("Success", "Configuration saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save config:\n{e}")
    
    def _on_closing(self):
        """Handle window close event."""
        if self.running:
            if messagebox.askokcancel(
                "Quit",
                "NJStayAwake is currently running. Do you want to stop and exit?"
            ):
                self._stop_service()
                self.root.destroy()
        else:
            self.root.destroy()


def main():
    """Launch the GUI application."""
    root = tk.Tk()
    app = StayAwakeGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
