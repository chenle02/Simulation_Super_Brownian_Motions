" noremap <leader><leader> :w!<cr>:cd ..<cr>:!make html<cr>
noremap <leader><leader> :let original_dir=getcwd()<cr>:w!<cr>:cd ..<cr>:!make html<cr>:!make latexpdf<cr>:cd <C-R>=original_dir<cr><cr>
