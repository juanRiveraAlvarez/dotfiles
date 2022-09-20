syntax on
set number
set mouse=a
set clipboard=unnamed
set showcmd
set ruler
set encoding=utf8
set showmatch
set sw=4
set relativenumber
let mapleader = " "
set laststatus=2
set backspace=2
set guioptions-=T
set guioptions-=L
set expandtab
set tabstop=2
set shiftwidth=2
set encoding=UTF-8
set colorcolumn=120
set nowrap
set ignorecase

call plug#begin('~/.vim/plugged')
Plug 'vim-airline/vim-airline'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'vim-airline/vim-airline-themes'
Plug 'ryanoasis/vim-devicons'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'preservim/nerdtree'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()


"maps Telescope
nnoremap ff :Telescope find_files<CR>
"maps nerdtree
nnoremap zz :NERDTreeToggle<CR>
"maps coc
nmap <silent> gd <Plug>(coc-definition)

let g:airline_powerline_fonts = 1

nnoremap sp :split<CR>
nnoremap fv :vs<CR>

inoremap <silent><expr> <cr> coc#pum#visible() ? coc#_select_confirm() : "\<C-g>u\<CR>"
" use <tab> for trigger completion and navigate to the next complete item
function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
