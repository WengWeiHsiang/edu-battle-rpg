# ROLE
你是一個資深 Python RPG engine engineer。

# CONTEXT
本專案是一個使用 Python + pygame 開發的教育型回合制 RPG。

玩家透過回答：
- 數學題
- 英文題
來進行戰鬥。

專案架構規範在 AGENTS.md。

必須遵守：
- modular architecture
- state machine
- separation of concerns
- quiz system 與 battle system 分離

# GOAL
（在這裡寫你要 Codex 做什麼）

例如：
建立 battle system 與 question system 的整合。

# REQUIREMENTS
- 使用 pygame
- battle logic 不可依賴 UI
- quiz system 必須獨立
- 使用 state machine
- 避免 massive main.py
- 必須可擴展

# FILES
允許修改：
- core/*
- states/*
- battle/*
- quiz/*
- entities/*
- ui/*

禁止：
- 重構整個專案
- 修改無關模組
- 打破現有架構

# IMPLEMENTATION RULES
- 保持 low coupling
- 優先 composition
- 每個 class 單一責任
- 小步修改
- 保持 readable code

# OUTPUT FORMAT
請：

1. 先說明設計
2. 再列出檔案變更
3. 最後逐檔案輸出完整 code

# VERIFICATION
完成後請檢查：

- state machine 是否正確
- quiz system 是否獨立
- battle system 是否與 UI 分離
- 是否有 circular dependency
- 是否符合 AGENTS.md

# 回復
本次用最小可執行骨架完成「battle system 與 question system 整合」，並維持 AGENTS.md 的邊界：

core/：主迴圈、pygame 初始化、state machine
states/：流程協調（Menu/Battle/Reward/Pause/GameOver）
battle/：純戰鬥規則（回合、傷害、勝負）
quiz/：純題目服務（出題、驗證）
ui/：純繪製與輸入緩衝，不含 gameplay 規則
entities/：共用資料模型（Combatant）
整合流程：

Player 回合輸入答案 -> quiz.validate_answer()
BattleState 將結果送入 battle.apply_quiz_answer()
Enemy 回合由 battle.run_enemy_turn() 自動執行
戰鬥結束後透過 state machine 轉到 RewardState 或 GameOverState
另外修正了 Pause -> Battle 進度遺失風險：改為「只有 MenuState 開戰時重置 battle」，暫停返回不重置。

