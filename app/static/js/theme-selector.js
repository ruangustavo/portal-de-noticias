(() => {
  'use strict'

  const getStoredTheme = () => localStorage.getItem('theme')
  const setStoredTheme = theme => localStorage.setItem('theme', theme)

  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
      return storedTheme
    }

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  const setTheme = theme => {
    if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.setAttribute('data-bs-theme', theme)
    } else {
      document.documentElement.setAttribute('data-bs-theme', theme)
    }
  }

  setTheme(getPreferredTheme())
 
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme()
    if (storedTheme !== 'light' && storedTheme !== 'dark') {
      setTheme(getPreferredTheme())
    }
  })

  window.addEventListener('DOMContentLoaded', () => {
    const moonIcon = document.querySelector('.ph-moon')

    moonIcon.addEventListener('click', () => {
      const currentTheme = getStoredTheme()
      const newTheme = currentTheme === 'light' ? 'dark' : 'light'
      setStoredTheme(newTheme)
      setTheme(newTheme)

      if (newTheme === 'dark') {
        moonIcon.classList.remove('ph-moon')
        moonIcon.classList.add('ph-sun')
      } else {
        moonIcon.classList.remove('ph-sun')
        moonIcon.classList.add('ph-moon')
      }
    })
  })
})();
