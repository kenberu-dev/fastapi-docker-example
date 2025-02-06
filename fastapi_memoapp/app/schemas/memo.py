from pydantic import BaseModel, Field

class InsertAndUpdateMemoSchema(BaseModel):
    title: str = Field(..., 
                       description="メモのタイトルを入力してください。少なくとも1文字以上必要です。", 
                       example="明日のアジェンダ", 
                       min_length=1, )
    description: str = Field(...,
                             description="メモの内容についての追加情報。任意で記入できます。",
                             example="会議で話すトピック：プロジェクトの進捗情報")

class MemoSchema(BaseModel):
    memo_id: int = Field(...,
                         description="メモを一いに識別するID番号。データーベースで自動的に割り当てられます。",
                         example=123)
    
class ResponseSchema(BaseModel):
    message: str = Field(...,
                         description="API操作の結果を説明するメッセージ。",
                         example="メモの更新に成功しました。")