# エラーが発生した場合にスクリプトを停止
$ErrorActionPreference = "Stop"

# 仮想環境が有効になっているか確認
if (-not (Test-Path .\venv\Scripts\activate.ps1)) {
    Write-Host "仮想環境が見つかりません。セットアップを実行してください。" -ForegroundColor Red
    exit 1
}

Write-Host "ビルドを開始します..."

# buildディレクトリが存在する場合のみ削除
if (Test-Path .\build) {
    Write-Host "既存のビルドディレクトリを削除中..."
    Remove-Item -Recurse -Force .\build
}

# distディレクトリが存在する場合は削除
if (Test-Path .\dist) {
    Write-Host "既存のdistディレクトリを削除中..."
    Remove-Item -Recurse -Force .\dist
}

try {
    Write-Host "アプリケーションをビルド中..."
    python setup.py build
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "ビルドが正常に完了しました！" -ForegroundColor Green
        Write-Host "ビルドされたファイルは build フォルダに格納されています。"
        
        # ビルドされたexeファイルのパスを表示
        $exePath = Get-ChildItem -Path .\build -Recurse -Filter "*.exe" | Select-Object -First 1
        if ($exePath) {
            Write-Host "実行ファイル: $($exePath.FullName)" -ForegroundColor Cyan
        }
    } else {
        Write-Host "ビルド中にエラーが発生しました。" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "エラーが発生しました: $_" -ForegroundColor Red
    exit 1
}