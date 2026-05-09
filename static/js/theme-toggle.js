function themeToggle() {
  return {
    theme: 'dark',
    init() {
      const stored = localStorage.getItem('theme');
      if (stored) {
        this.theme = stored;
      }
      document.documentElement.classList.toggle('dark', this.theme === 'dark');
    },
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.classList.toggle('dark', this.theme === 'dark');
      localStorage.setItem('theme', this.theme);
    },
  };
}
