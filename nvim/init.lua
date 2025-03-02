vim.opt.number = true
vim.opt.mouse = a
vim.opt.clipboard=unnamed
vim.opt.encoding=utf8
vim.opt.sw=4
vim.opt.relativenumber=true
vim.opt.laststatus=2
vim.opt.backspace="2"
vim.opt.expandtab = true
vim.opt.tabstop=8
vim.opt.shiftwidth=2
vim.opt.shortmess =c
vim.opt.showcmd = true
vim.opt.ruler = true
vim.opt.showmatch = true
vim.opt.wrap = false

local home = os.getenv('HOME')

local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

local conf = {}
conf.header = {
  "                                                       ",
  "                                                       ",
  "                                                       ",
  "            ▐ ▄ ▄▄▄ .       ▌ ▐·▪  • ▌ ▄ ·.            ",
  "             •█▌▐█▀▄.▀·▪     ▪█·█▌██ ·██ ▐███▪         ",
  "             ▐█▐▐▌▐▀▀▪▄ ▄█▀▄ ▐█▐█•▐█·▐█ ▌▐▌▐█·         ",
  "             ██▐█▌▐█▄▄▌▐█▌.▐▌ ███ ▐█▌██ ██▌▐█▌         ",
  "             ▀▀ █▪ ▀▀▀  ▀█▄▀▪. ▀  ▀▀▀▀▀  █▪▀▀▀         ",
  "                                                       ",
  "                                                       ",
  "                  Config by Juan Rivera                ",
  "                                                       ",
  "                                                       ",
  "                                                       ",
  "                                                       ",
}
conf.center = {
  {
    icon = "󰈞  ",
    desc = "Find  File                              ",
    action = "Neotree toggle",
    key = "f f",
  },
  {
    icon = "  ",
    desc = "Open Nvim config                        ",
    action = "tabnew $MYVIMRC | tcd %:p:h",
    key = "<Leader> e v",
  },
  {
    icon = "  ",
    desc = "New file                                ",
    action = "enew",
    key = "e",
  },
  {
    icon = "󰗼  ",
    desc = "Quit Nvim                               ",
    -- desc = "Quit Nvim                               ",
    action = "qa",
    key = "q",
  },
}

require("lazy").setup({
  {
    'nvim-telescope/telescope.nvim', tag = '0.1.8',
    requires = { {'nvim-lua/plenary.nvim'} }
  },
  {
  'nvimdev/dashboard-nvim',
    event = 'VimEnter',
    config = function()
    require('dashboard').setup {
      theme = 'doom',
      shortcut_type = 'number',
      config = conf
    }
    end,
    dependencies = { {'nvim-tree/nvim-web-devicons'}}
  },
  {
  "glepnir/lspsaga.nvim",
  event = "LspAttach",
  config = function()
    require("lspsaga").setup({
      ui = {
        border = "rounded", -- Bordes redondeados en las alertas
        title = true,
        devicon = true,
      },
      lightbulb = {
        enable = true, -- Muestra un bombillo si hay acciones disponibles
        sign = true,
      },
      diagnostic = {
        virtual_text = false, -- Evita que las alertas se vean encima del código
        signs = true,
        underline = true,
        float = {
          border = "rounded",
        },
      },
    })
  end,
  dependencies = { { "nvim-tree/nvim-web-devicons" } },
  },
  {'MaximilianLloyd/ascii.nvim', requires = {
	"MunifTanjim/nui.nvim"}
  },
  {'hrsh7th/vim-vsnip'},
  {'hrsh7th/vim-vsnip-integ'},
--  { "ellisonleao/gruvbox.nvim", priority = 1000 , config = true},
  {"sainnhe/gruvbox-material"},

  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    event = "VeryLazy",
    main = "nvim-treesitter.configs",
    opts = {
      ensure_installed = {
        "javascript",
        "java",
        "typescript",
        "python",
      },
      highlight = {
        enable = true,
      },
      ident = {
        enable = true,
      },
    },
  },
  {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' }
  },
  {'hrsh7th/cmp-nvim-lsp'},
  {'hrsh7th/cmp-buffer'},
  {'hrsh7th/cmp-path'},
  {'hrsh7th/cmp-cmdline'},
  {'hrsh7th/nvim-cmp'},
  {"L3MON4D3/LuaSnip"},
--  {"morhetz/gruvbox"},
  {'williamboman/mason.nvim',
    config = true,
  },
  {'williamboman/mason-lspconfig.nvim'},
  {"neovim/nvim-lspconfig"},
  {"nvim-neo-tree/neo-tree.nvim",
	dependencies = {
    	"nvim-lua/plenary.nvim",
      	"nvim-tree/nvim-web-devicons",
      	"MunifTanjim/nui.nvim",
  	},
	keys = {
      		{ "zz", "<cmd>Neotree toggle<cr>", desc = "NeoTree" },
    	},
    	config = function()
      		require("neo-tree").setup()
    	end,
	}
})


local on_attach = function(_,bufnr)
  vim.bo[bufnr].omnifunc = 'v:lua.vim.lsp.omnifunc'
  vim.keymap.set('n','gi',vim.lsp.buf.implementation,{buffer = bufnr})
  vim.keymap.set("n", "gd", vim.lsp.buf.definition, { buffer = bufnr, desc = "Go to Definition" })
  vim.keymap.set("n", "gr", vim.lsp.buf.references, { buffer = bufnr, desc = "Find References" })
  vim.keymap.set('n','ft', function()
    vim.lsp.buf.format {async = true}
  end, {buffer = bufnr})
end

--require'lspconfig'.eslint.setup{
--  on_attach = function(client, bufnr)
--    vim.api.nvim_create_autocmd("BufWritePre", {
--      buffer = bufnr,
--      command = "EslintFixAll",
--    })
--  end,
--}

--require'lspconfig'.tsserver.setup{
--  on_attach = on_attach,
--  init_options = {
--    plugins = {
--      {
--        name = "@vue/typescript-plugin",
--        location = "/usr/local/lib/node_modules/@vue/typescript-plugin",
--        languages = {"javascript", "typescript", "vue", "tsx"},
--      },
--    },
--  },
--  filetypes = {
--    "javascript",
--    "typescript",
--    "typescriptreact",
--    "typescript.tsx",
--    "vue",
--  },
--}

--require'lspconfig'.lemminx.setup{
--  on_attach = on_attach,
--}

--require'lspconfig'.clangd.setup{
--  on_attach = on_attach,
--}

--Enable (broadcasting) snippet capability for completion
--local capabilities = vim.lsp.protocol.make_client_capabilities()
--capabilities.textDocument.completion.completionItem.snippetSupport = true

--require'lspconfig'.html.setup {
--  on_attach = on_attach,
--  capabilities = capabilities,
--}


--require'lspconfig'.cssls.setup {
--on_attach = on_attach,
--capabilities = capabilities,
--}

--require'lspconfig'.pyright.setup{
--  on_attach = on_attach,
--}
--
local lombok_path = vim.fn.expand("~/.local/share/lombok/lombok.jar")

require'lspconfig'.jdtls.setup{ 
  root_dir = require("lspconfig").util.root_pattern("pom.xml", "build.py", "gradle.build", ".git","src"),
  on_attach = on_attach,
  cmd = { 
    'jdtls',
    '-Xmx1Ga',
--    '-javaagent:' .. home .. '/.local/share/eclipse/lombok.jar',
    '--jvm-arg=-javaagent:' .. lombok_path, 
    '-jar $(echo "$JAR")',
  },
  settings = {
    java = {
      project = {
        referencedLibraries = {
          "lib/**/*.jar"
        },
        sourcePaths = { "src" }
      },
      errors = {
        incompleteClasspath = "ignore"
      }
    }
  }
}

local cmp = require'cmp'

cmp.setup({
    snippet = {
      -- REQUIRED - you must specify a snippet engine
      expand = function(args)
        vim.fn["vsnip#anonymous"](args.body) -- For `vsnip` users.
        -- require('luasnip').lsp_expand(args.body) -- For `luasnip` users.
        -- require('snippy').expand_snippet(args.body) -- For `snippy` users.
        -- vim.fn["UltiSnips#Anon"](args.body) -- For `ultisnips` users.
        -- vim.snippet.expand(args.body) -- For native neovim snippets (Neovim v0.10+)
      end,
    },
    window = {
      -- completion = cmp.config.window.bordered(),
      -- documentation = cmp.config.window.bordered(),
    },
    mapping = cmp.mapping.preset.insert({
      ['<Tab>'] = cmp.mapping.select_next_item({ behavior = cmp.SelectBehavior.Insert }),
      ['<C-f>'] = cmp.mapping.scroll_docs(4),
      ['<C-Space>'] = cmp.mapping.complete(),
      ['<C-e>'] = cmp.mapping.abort(),
      ['<CR>'] = cmp.mapping.confirm({ select = true }), -- Accept currently selected item. Set `select` to `false` to only confirm explicitly selected items.
    }),
    sources = cmp.config.sources({
      { name = 'nvim_lsp' },
      { name = 'vsnip' }, -- For vsnip users.
      -- { name = 'luasnip' }, -- For luasnip users.
      -- { name = 'ultisnips' }, -- For ultisnips users.
      -- { name = 'snippy' }, -- For snippy users.
    }, {
      { name = 'buffer' },
    })
  })

require('lualine').setup {
  options = {
    icons_enabled = true,
    theme = 'auto',
    component_separators = { left = ' | ', right = ' | '},
    section_separators = { left = '', right = ''},
    disabled_filetypes = {
      statusline = {},
      winbar = {},
    },
    ignore_focus = {},
    always_divide_middle = true,
    globalstatus = false,
    refresh = {
      statusline = 1000,
      tabline = 1000,
      winbar = 1000,
    }
  },
  sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch', 'diff'},
    lualine_c = {'filename'},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  },
  tabline = {
     lualine_a = {'buffers'},
      lualine_z = {'tabs'}
  },
  winbar = {},
  inactive_winbar = {},
  extensions = {}
}


vim.opt.termguicolors = true
vim.o.background = "dark" -- or "light" for light mode
vim.cmd.colorscheme('gruvbox-material')

vim.cmd [[
  highlight DiagnosticVirtualTextError guifg=#FF5555 gui=bold
  highlight DiagnosticVirtualTextWarn guifg=#458588 gui=bold
  highlight DiagnosticVirtualTextInfo guifg=#00FFFF gui=bold
  highlight DiagnosticVirtualTextHint guifg=#50FA7B gui=italic
]]

vim.api.nvim_set_hl(0, "DiagnosticSignError", { fg = "#FF5555", bg = "NONE" })
vim.api.nvim_set_hl(0, "DiagnosticSignWarn", { fg = "#458588", bg = "NONE" })
vim.api.nvim_set_hl(0, "DiagnosticSignInfo", { fg = "#00FFFF", bg = "NONE" })
vim.api.nvim_set_hl(0, "DiagnosticSignHint", { fg = "#50FA7B", bg = "NONE" })


local signs = { Error = "✘", Warn = "⚠", Hint = "💡", Info = "ℹ" }
for type, icon in pairs(signs) do
  local hl = "DiagnosticSign" .. type
  vim.fn.sign_define(hl, { text = icon, texthl = hl, numhl = hl })
end


vim.keymap.set('n', 'zj', '<cmd>bprevious<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'zk', '<cmd>bnext<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'zq', '<cmd>bdelete<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'tt', '<cmd>term<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'fv', '<cmd>vs<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'sp', '<cmd>split<cr>', {desc = 'Open terminal'})

local builtin = require('telescope.builtin')
vim.keymap.set('n', 'ff', builtin.find_files, { desc = 'Telescope find files' })
vim.keymap.set('n', 'fb', builtin.buffers, { desc = 'Telescope buffers' })
