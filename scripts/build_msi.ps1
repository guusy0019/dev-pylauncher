# エラーが発生した場合にスクリプトを停止
$ErrorActionPreference = "Stop"

Write-Host "MSIインストーラーのビルドを開始します..." -ForegroundColor Cyan

# distディレクトリが存在する場合、プロセスを終了してから削除
if (Test-Path .\dist) {
    Write-Host "既存のdistディレクトリを削除中..."
    
    # 実行中のプロセスを終了
    $exeName = "pylauncher.exe"
    $processes = Get-Process | Where-Object { $_.Path -like "*$exeName" }
    if ($processes) {
        Write-Host "実行中のプロセスを終了しています..."
        $processes | ForEach-Object { $_.Kill() }
        # プロセスが完全に終了するのを待つ
        Start-Sleep -Seconds 2
    }

    # 削除を試みる
    try {
        Remove-Item -Recurse -Force .\dist -ErrorAction Stop
    } catch {
        Write-Host "distディレクトリの削除に失敗しました。手動で削除してください。" -ForegroundColor Yellow
        Write-Host "削除後、任意のキーを押してください..."
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    }
}

try {
    Write-Host "MSIインストーラーを作成中..."
    python setup.py bdist_msi
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "MSIインストーラーの作成が完了しました！" -ForegroundColor Green
        
        # 作成されたMSIファイルのパスを表示
        $msiPath = Get-ChildItem -Path .\dist -Filter "*.msi" | Select-Object -First 1
        if ($msiPath) {
            Write-Host "MSIファイル: $($msiPath.FullName)" -ForegroundColor Cyan
            
            # エクスプローラーでMSIファイルがあるフォルダを開く
            Write-Host "distフォルダを開きます..."
            Invoke-Item .\dist
        }
    } else {
        Write-Host "MSIインストーラーの作成中にエラーが発生しました。" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "エラーが発生しました: $_" -ForegroundColor Red
    exit 1
}
