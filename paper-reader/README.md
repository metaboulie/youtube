# The very first dream paper reader

[Watch the video 🤓](https://www.youtube.com/watch?v=qZzK-2GQq7k)

## Setup

1. First, you need to have `neovim` installed and configured.

I suggest watching the video by
[Josean Martinez](https://www.youtube.com/watch?v=6pAG3BHurdM&t=3170s) to get your
Neovim environment set up if you haven't already.

2. Optional but recommended: Install `MeanderingProgrammer/render-markdown.nvim` to
   render markdown in visual mode and use `stevearc/conform.nvim` together with
   `prettier` to format markdown.

If you use `lazy.nvim`, add the following:

```lua
{
  "MeanderingProgrammer/render-markdown.nvim",
  "stevearc/conform.nvim",
}
```

you can check my configuration here for [markdown](./src/markdown.lua) and
[formatting](./src/formatting.lua).

3. If you don't have prettier installed, you can install it by
   `npm install -g prettier`.

Further, you can configure prettier by editing `.prettierrc`.

Here is my configuration for `.prettierrc`:

```json
{
    "proseWrap": "always",
    "printWidth": 79,
    "tabWidth": 4
}
```

4. Install all packages we will use in this project.

```fish
brew install uv ollama
uv install python 3.11
uv init
uv add --dev ruff
uv add docling ell-ai
ollama pull qwen2.5:0.5b
```

5. Use `docling` to transform an Arxiv paper to markdown.

```fish
uv run docling <arxiv-paper-pdf-url>
```

6. Chat with the paper.

```fish
ollama serve
uv run src/paper_chat.py <path-to-paper-markdown-file> <path-to-output-file>
```
