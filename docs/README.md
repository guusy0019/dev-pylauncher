# dev_windows_app

### tree

```
├─app
│  ├─assets
│  │  ├─data
│  │  └─images
│  ├─config
│  │  └─__pycache__
│  ├─module
│  │  ├─model
│  │  ├─repository
│  │  ├─service
│  │  ├─usecase
│  │  └─utility
│  └─ui
│      ├─layout
│      │  └─__pycache__
│      ├─page
│      │  └─__pycache__
│      ├─route
│      │  └─__pycache__
│      ├─widget
│      │  └─__pycache__
│      └─__pycache__
├─build
│  └─main
│      └─localpycs
├─dist
├─docs
├─logs
├─scripts
│  ├─linux
│  └─windows
└─venv

```

```shell
Python -V 3.12.5
```

```mermaid
graph TD
    %% メインの階層
    subgraph "アーキテクチャ"
        subgraph "UI"
            layout["layout"]
            page["page"]
            layout --> page
        end

        subgraph "infrastracture"
            repository["repository"]
        end

        subgraph "application"
            usecase["usecase"]
            interface["interface"]
        end

        subgraph "domain"
            model["model"]
        end
    end

    %% レイヤー間の接続
    page --> usecase
    repository -.-> interface
    usecase --> model
    repository -- DI --> page
```

### 参考にしたレイアウトのコード

[公式の example](https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/image_example.py)
