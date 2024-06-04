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

require("lazy").setup({
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
  {"morhetz/gruvbox"},
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
  vim.keymap.set('n','gd',vim.lsp.buf.definition,{buffer = bufnr})
  vim.keymap.set('n','gi',vim.lsp.buf.implementation,{buffer = bufnr})
end

require'lspconfig'.pylsp.setup{
  on_attach = on_attach,
  settings = {
    pylsp = {
      plugins = {
        pycodestyle = {
          ignore = {'W391'},
          maxLineLength = 100
        }
      }
    }
  }
}
require'lspconfig'.jdtls.setup{ 
  on_attach = on_attach,
  cmd = { 'jdtls' } 
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
vim.cmd.colorscheme('gruvbox')

vim.keymap.set('n', 'zj', '<cmd>bprevious<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'zk', '<cmd>bnext<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'zq', '<cmd>bdelete<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'tt', '<cmd>term<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'fv', '<cmd>vs<cr>', {desc = 'Open terminal'})
vim.keymap.set('n', 'sp', '<cmd>split<cr>', {desc = 'Open terminal'})