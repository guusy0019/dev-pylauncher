param (
    [ValidateSet("development", "production")]
    [string]$Environment = "production"  # デフォルトはproduction
)

# エラーが発生した場合にスクリプトを停止
$ErrorActionPreference = "Stop"

# 環境変数を設定
Write-Host "環境変数を設定中..." -ForegroundColor Cyan

# 環境に応じた設定
switch ($Environment) {
    "development" {
        $env:LAUNCH_MODE = "DEBUG"
        Write-Host "開発モードでビルドします" -ForegroundColor Yellow
    }
    "production" {
        $env:LAUNCH_MODE = "PROD"
        Write-Host "本番モードでビルドします" -ForegroundColor Yellow
    }
    default {
        Write-Host "未知の環境が指定されました: $Environment" -ForegroundColor Red
        exit 1
    }
}

try {
    # ビルドプロセスを実行
    Write-Host "ビルドプロセスを開始します..." -ForegroundColor Cyan
    
    if ($Environment -eq "production") {
        # 本番環境用のビルド
        Write-Host "本番用のビルドを実行中..." -ForegroundColor Yellow
        .\scripts\build_exe.ps1
        if ($LASTEXITCODE -eq 0) {
            .\scripts\build_msi.ps1
        }
    } else {
        # 開発環境用のビルド
        Write-Host "開発用のビルドを実行中..." -ForegroundColor Yellow
        .\scripts\build_exe.ps1
    }
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nビルドが完了しました！" -ForegroundColor Green
    } else {
        Write-Host "`nビルドに失敗しました。" -ForegroundColor Red
        exit 1
    }
} finally {
    # 環境変数をクリア
    Remove-Item Env:LAUNCH_MODE -ErrorAction SilentlyContinue
}
