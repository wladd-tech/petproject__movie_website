/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './apps/**/*.html',
    './templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'background-black': '#171718',
      }
    },
  },
  plugins: [],
}

