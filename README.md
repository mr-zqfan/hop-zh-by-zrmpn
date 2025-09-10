#### 介绍
- 只能在 Neovim 中运行, 包括 [vscode-neovim](https://github.com/vscode-neovim/vscode-neovim).
- 本插件是[hop.nvim](https://github.com/phaazon/hop.nvim)的一个扩展(extension), 它能让[hop.nvim](https://github.com/phaazon/hop.nvim)识别中文, 它必须依赖[hop.nvim](https://github.com/phaazon/hop.nvim)才能运行, 查看[vim-easymotion-zh](https://github.com/zzhirong/vim-easymotion-zh)获取更详细的介绍.
- 双拼自然码，但有魔然的个别改键，如 几 ji，但实际是 jo，查看[rime-moran](https://github.com/rimeinn/rime-moran)获取更多信息.
- 编码文件参考本仓库的 `moran_fixed_simp.dict.yaml`
- 改编码，可参考 conv.py 的实现自行转换
- 强烈推荐空格作为 HopZrmpy2 降级到 HopZrmpy1 的触发键，因为打字也用空格选字

#### 安装
- 本插件不可独立运行, 它依赖于[hop.nvim](https://github.com/phaazon/hop.nvim).
- 使用 [lazy.nvim](https://github.com/folke/lazy.nvim) 进行安装:
```lua
return {
    'mr-zqfan/hop-zh-by-zrmpy',
    dependencies = {
        'phaazon/hop.nvim',
    },
    config = function()
        local hop_zrmpy = require"hop-zh-by-zrmpy"
        hop_zrmpy.setup({
            -- 注意: 本扩展的默认映射覆盖掉了一些常用的映射: f, F, t, T, s
            -- 设置 set_default_mappings 为 false 可关闭默认映射.
            -- 个人建议关闭，因为 cf. 等操作也会用到 f, F, t, T
            set_default_mappings = false,
        })
    end
}
```

- 使用 Plug
```vim
" Plug {
    call plug#begin()
    Plug 'phaazon/hop.nvim'
    Plug 'mr-zqfan/hop-zh-by-zrmpn'
    call plug#end()
" }
```

#### 配置
- 将此扩展加入[hop.nvim](https://github.com/phaazon/hop.nvim) extension 配置项.
- 使用 lazy 配置样例:
```lua
return{
    'phaazon/hop.nvim',
    branch = 'v1',
    config = function()
        local hop = require('hop')
        hop.setup {
            keys = 'fjdkslghturieow',
            char2_fallback_key = ' ',
            extensions = {
                'hop-zh-by-zrmpy',
            },
        }
    end,
}
```

- 使用 packer 的配置样例:
```vim
" hop.nvim {
    nmap <silent> <space> :HopZrmpy2MW<CR>
    vmap <silent> <space> <cmd>HopZrmpy2MW<CR>

    nmap <silent> ' :HopLine<CR>
    vmap <silent> ' <cmd>HopLine<CR>
" }
```
```lua
-- hop-zh-by-zrmpy {
  require("hop-zh-by-zrmpy").setup({
      -- 注意: 本扩展的默认映射覆盖掉了一些常用的映射: f, F, t, T, s
      -- 设置 set_default_mappings 为 false 可关闭默认映射.
      -- 个人建议关闭，因为 cf. 等操作也会用到 f, F, t, T
      set_default_mappings = false,
  })
-- }

-- packer {
  vim.cmd [[packadd packer.nvim]]
  return require('packer').startup(function(use)
    -- Packer can manage itself
    use 'wbthomason/packer.nvim'

    -- Do not forget the 'PackerCompile' command!
    use {
      'phaazon/hop.nvim',
      branch = 'v2', -- optional but strongly recommended
      config = function()
        -- you can configure Hop the way you like here; see :h hop-config
        require'hop'.setup {
          keys = "asghlqwertyuiopzxcvbnm;',./kdjf",
          char2_fallback_key = ' ',
          extensions = {
            'hop-zh-by-zrmpy',
          },
        }
      end
    }
  end)
-- }
```

#### 使用
- 通过命令: 本扩展创建了 `HopZrmpy1*`, `HopZrmpy2*`, 比如`:HopZrmpy1`.
- 通过调用 api: `hop_zh_by_zrmpy.hint_char1({opts})` 和 `hop_zh_by_zrmpy.hint_char2({opts})`, 比如, `:lua require'hop-zh-by-zrmpy.hint_char1()`, 帮助文档请查看`hop.hint_char1`和`hop.hint_char2`, 
- 通过默认/自定义映射:
    - 默认设置`set_default_mappings`为`true`:
        - `f`, `F`, `T`, `t`: 功能与覆盖前相同, 只不过多了跳转目标.
        - `s`映射成`require'hop-zh-by-zrmpy'.hint_char2()`.

#### 帮助
- 查看[hop.nvim](https://github.com/phaazon/hop.nvim)对应命令帮助文档, 比如, 想要查看`HopZrmpy1`帮助, 
