/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html",],
  theme: {
    extend: {
      colors: {
        'primary':'#ff2d87',
        'secondary':'#0d3662',
        'offWhite':'#f7f8fb',
        'lightBlue':'#e1e9fa',
        'accentPink':'#ffd6dd',
        'gray2':'#858494;',
        'checkGreen': '#9be48c',
        'whatsapp': '#25d366',
        'facebook': '#4267b2',
        'snapchat': '#fdfa42',
        'messenger':'#00b2ff',
        'warning' : '#ffd66b',
        'black' : '#0c092a'
   },
    },
  },
  plugins: [],
}
