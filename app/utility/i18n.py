import json
import os

from app.config.settings import LOCALE_DIR


class I18n:
    _instance = None
    _translations: dict[str, dict[str, any]] = {}
    _current_lang = "ja"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(I18n, cls).__new__(cls)
            cls._instance._load_translations()
        return cls._instance

    def _load_translations(self):
        """利用可能な言語ファイルをすべて読み込む"""
        for file in os.listdir(LOCALE_DIR):
            if file.endswith(".json"):
                lang = file.split(".")[0]
                with open(os.path.join(LOCALE_DIR, file), "r", encoding="utf-8") as f:
                    self._translations[lang] = json.load(f)

    @classmethod
    def get_text(cls, key: str, lang: str = None) -> str:
        """
        指定されたキーの翻訳テキストを取得
        key: ドット区切りのキー（例: "menu.home"）
        lang: 言語コード（指定がない場合は現在の言語を使用）
        """
        if lang is None:
            lang = cls._current_lang

        # キーをドットで分割して階層的にアクセス
        keys = key.split(".")
        value = cls._translations.get(lang, {})
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, key)
            else:
                return key
        return value if isinstance(value, str) else key

    @classmethod
    def set_language(cls, lang: str):
        """使用する言語を設定"""
        if lang in cls._translations:
            cls._current_lang = lang

    @classmethod
    def get_available_languages(cls) -> list:
        """利用可能な言語のリストを取得"""
        return list(cls._translations.keys()) 