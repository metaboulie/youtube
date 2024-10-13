return {
	"MeanderingProgrammer/render-markdown.nvim",
	opts = {},
	dependencies = { "nvim-treesitter/nvim-treesitter", "echasnovski/mini.nvim" }, -- if you use the mini.nvim suite
	config = function()
		require("render-markdown").setup({
			bullet = { right_pad = -1 },
			callout = {
				note = { raw = "[!NOTE]", rendered = "󰋽 Note", highlight = "RenderMarkdownInfo" },
				tip = { raw = "[!TIP]", rendered = "󰌶 Tip", highlight = "RenderMarkdownSuccess" },
				important = { raw = "[!IMPORTANT]", rendered = "󰅾 Important", highlight = "RenderMarkdownHint" },
				warning = { raw = "[!WARNING]", rendered = "󰀪 Warning", highlight = "RenderMarkdownWarn" },
				caution = { raw = "[!CAUTION]", rendered = "󰳦 Caution", highlight = "RenderMarkdownError" },
				abstract = { raw = "[!ABSTRACT]", rendered = "󰨸 Abstract", highlight = "RenderMarkdownInfo" },
				summary = { raw = "[!SUMMARY]", rendered = "󰨸 Summary", highlight = "RenderMarkdownInfo" },
				tldr = { raw = "[!TLDR]", rendered = "󰨸 Tldr", highlight = "RenderMarkdownInfo" },
				info = { raw = "[!INFO]", rendered = "󰋽 Info", highlight = "RenderMarkdownInfo" },
				todo = { raw = "[!TODO]", rendered = "󰗡 Todo", highlight = "RenderMarkdownInfo" },
				hint = { raw = "[!HINT]", rendered = "󰌶 Hint", highlight = "RenderMarkdownSuccess" },
				success = { raw = "[!SUCCESS]", rendered = "󰄬 Success", highlight = "RenderMarkdownSuccess" },
				check = { raw = "[!CHECK]", rendered = "󰄬 Check", highlight = "RenderMarkdownSuccess" },
				done = { raw = "[!DONE]", rendered = "󰄬 Done", highlight = "RenderMarkdownSuccess" },
				question = { raw = "[!QUESTION]", rendered = "󰘥 Question", highlight = "RenderMarkdownWarn" },
				help = { raw = "[!HELP]", rendered = "󰘥 Help", highlight = "RenderMarkdownWarn" },
				faq = { raw = "[!FAQ]", rendered = "󰘥 Faq", highlight = "RenderMarkdownWarn" },
				attention = { raw = "[!ATTENTION]", rendered = "󰀪 Attention", highlight = "RenderMarkdownWarn" },
				failure = { raw = "[!FAILURE]", rendered = "󰅖 Failure", highlight = "RenderMarkdownError" },
				fail = { raw = "[!FAIL]", rendered = "󰅖 Fail", highlight = "RenderMarkdownError" },
				missing = { raw = "[!MISSING]", rendered = "󰅖 Missing", highlight = "RenderMarkdownError" },
				danger = { raw = "[!DANGER]", rendered = "󱐌 Danger", highlight = "RenderMarkdownError" },
				error = { raw = "[!ERROR]", rendered = "󱐌 Error", highlight = "RenderMarkdownError" },
				bug = { raw = "[!BUG]", rendered = "󰨰 Bug", highlight = "RenderMarkdownError" },
				example = { raw = "[!EXAMPLE]", rendered = "󰉹 Example", highlight = "RenderMarkdownHint" },
				quote = { raw = "[!QUOTE]", rendered = "󱆨 Quote", highlight = "RenderMarkdownQuote" },
				cite = { raw = "[!CITE]", rendered = "󱆨 Cite", highlight = "RenderMarkdownQuote" },
				recall = { raw = "[!RECALL]", rendered = "󰋽 Recall", highlight = "RenderMarkdownInfo" },
				design = { raw = "[!DESIGN]", rendered = "󰉹 Desgin", highlight = "RenderMarkdownInfo" },
				suggestion = { raw = "[!SUGGESTION]", rendered = "󰉹 Suggestion", highlight = "RenderMarkdownHint" },
				feedback = { raw = "[!FEEDBACK]", rendered = "󰉹 Feedback", highlight = "RenderMarkdownInfo" },
			},
			checkbox = {
				unchecked = { icon = "✘ " },
				checked = { icon = "✔ " },
				custom = {
					optional = { raw = "[-]", rendered = "󰥔 ", highlight = "RenderMarkdownTodo" }, -- Optional task
					todo = { raw = "[+]", rendered = "⬜ ", highlight = "RenderMarkdownTodo" }, -- To-do task
					urgent = { raw = "[!]", rendered = "⚡", highlight = "RenderMarkdownUrgent" }, -- Urgent task
					in_progress = { raw = "[~]", rendered = "⟳ ", highlight = "RenderMarkdownInProgress" }, -- In-progress task
					deferred = { raw = "[>]", rendered = "⏳", highlight = "RenderMarkdownDeferred" }, -- Deferred task
				},
			},
			code = { enabled = false },
			dash = { icon = "=" },
			heading = {
				position = "inline",
				icons = { "󰼏 ", "󰎨 " },
				border = true,
				border_virtual = true,
			},
			pipe_table = { enabled = false },
		})
	end,
}
