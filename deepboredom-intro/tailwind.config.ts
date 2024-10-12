import type { Config } from 'tailwindcss';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		colors: {
			nord: {
				// Polar Night (darkest to lightest)
				'bg-darkest': '#2E3440', // nord0
				'bg-darker': '#3B4252', // nord1
				'bg-dark': '#434C5E', // nord2
				'bg-light': '#4C566A', // nord3
				'bg-warp': '#012B36', // warp

				// Snow Storm (darkest to lightest)
				'fg-dark': '#D8DEE9', // nord4
				'fg-medium': '#E5E9F0', // nord5
				'fg-light': '#ECEFF4', // nord6

				// Frost
				'frost-1': '#8FBCBB', // nord7
				'frost-2': '#88C0D0', // nord8
				'frost-3': '#81A1C1', // nord9
				'frost-4': '#5E81AC', // nord10

				// Aurora
				'aurora-red': '#BF616A', // nord11
				'aurora-orange': '#D08770', // nord12
				'aurora-yellow': '#EBCB8B', // nord13
				'aurora-green': '#A3BE8C', // nord14
				'aurora-purple': '#B48EAD' // nord15
			},
			// Primary use color: for main interactive elements (buttons, links, etc.)
			primary: '#1a1a2e',

			// Background color: used for the main content background
			background: '#0f0e17',

			// Main text color for contrast against dark backgrounds
			foreground: '#e0fbfc',

			// Accent color: used for highlighting or hover effects
			accent: '#ff6f61',

			// Border color for inputs, containers, etc.
			border: '#98C1D9',

			// Hover effect on interactive elements (buttons, links)
			hover: '#ee6c4d',

			success: '#3CAEA3', // For success messages or positive indicators
			warning: '#ff7f11', // Warning or caution elements (alerts, buttons)
			error: '#d90429', // Error messages or destructive actions (delete buttons)
			muted: '#555555', // Muted text for secondary information

			// Neutral shades: used for secondary text, borders, or cards
			neutral: {
				100: '#e4e4e4', // Light gray for text on dark backgrounds
				200: '#c1c1c1', // Mid-gray for subtle contrasts
				300: '#737373', // Darker gray for less attention-seeking content
				400: '#2b2b2b' // Almost black, good for card borders or divisions
			}
		},
		fontFamily: {
			// Fonts for different sections of the website

			// Title: used for large, impactful headings
			'font-title': ['"Iosevka"', 'monospace'],

			// Header: used for subheadings or prominent labels
			'font-header': ['"Lekton"', 'sans-serif'],

			// Paragraph text: regular reading text
			'font-p': ['"Georgia"', 'serif'],

			// Optional for buttons or captions where minimalistic look is required
			'font-caption': ['"Inter"', 'sans-serif']
		},
		extend: {
			// Spacing design based on a multiple-based scaling system
			spacing: {
				'1': '0.25rem', // 4px
				'2': '0.5rem', // 8px
				'3': '0.75rem', // 12px
				'4': '1rem', // 16px
				'5': '1.25rem', // 20px
				'6': '1.5rem', // 24px
				'8': '2rem', // 32px
				'10': '2.5rem', // 40px
				'12': '3rem', // 48px
				'16': '4rem', // 64px
				'20': '5rem', // 80px
				'24': '6rem', // 96px
				'32': '8rem', // 128px
				'40': '10rem', // 160px
				'48': '12rem', // 192px
				'56': '14rem', // 224px
				'64': '16rem', // 256px
				'72': '18rem', // 288px
				'80': '20rem', // 320px
				'96': '24rem', // 384px
				// Extra-large custom spacings for advanced layouts
				'128': '32rem', // 512px
				'144': '36rem', // 576px
				'160': '40rem', // 640px
				'192': '48rem', // 768px
				'256': '64rem', // 1024px
				'8xl': '96rem', // 1536px
				'9xl': '128rem' // 2048px
			},
			// Comprehensive border radius design
			borderRadius: {
				sm: '0.125rem', // Small radius for tiny elements (2px)
				md: '0.375rem', // Default medium rounding (6px)
				lg: '0.5rem', // Large radius for noticeable rounding (8px)
				xl: '1rem', // Extra-large radius for components (16px)
				'2xl': '1.5rem', // Larger elements like modals (24px)
				'3xl': '2rem', // Cards, containers (32px)
				'4xl': '3rem', // Very large elements, full rounding (48px)
				full: '9999px' // Full rounding for pills or circular elements
			},
			keyframes: {
				'fade-fly-up': {
					'0%': { opacity: '0', transform: 'translateY(20px)' },
					'100%': { opacity: '1', transform: 'translateY(0)' }
				},
				'fade-fly-down': {
					'0%': { opacity: '0', transform: 'translateY(-20px)' },
					'100%': { opacity: '1', transform: 'translateY(0)' }
				},
				'zoom-in': {
					'0%': { opacity: '0', transform: 'scale(0.5)' },
					'100%': { opacity: '1', transform: 'scale(1)' }
				},
				'zoom-out': {
					'0%': { opacity: '1', transform: 'scale(1)' },
					'100%': { opacity: '0', transform: 'scale(0.5)' }
				}
			},
			animation: {
				'fade-fly-up': 'fade-fly-up 1s ease-out',
				'fade-fly-down': 'fade-fly-down 1s ease-out',
				'zoom-in': 'zoom-in 1.5s ease-out forwards',
				'zoom-out': 'zoom-out 2s ease-in-out forwards'
			}
		}
	},
	plugins: []
} satisfies Config;
