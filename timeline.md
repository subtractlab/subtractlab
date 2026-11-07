# MeaningSpace / DP Multi-Agent — Prior-Art Timeline（先行実装タイムライン）

**First published: 2026-07-16 (JST) / SubtractLab（開発者1名 + AI）**

各機構の設計・実装・実証の確定日を記録する。出典はMeaningSpace内の結晶（作成日時つき構造化開発記録、2026-07-16時点で1,983個）。本リポジトリのgitコミット履歴が第三者検証可能なタイムスタンプとして機能する。HTML版: [history.html](https://subtractlab.com/history.html)

## Era 1 — AIとの対話、業務自動化からの出発
| 日付 | 出来事 |
|---|---|
| 2023-02 | AIとの対話を始める（ChatGPT）— 最初の会話は 2023-02-07。この時期の ChatGPT との会話 1,567 件も、のちに MeaningSpace に取り込んだ |
| 2024-09 | Claudeによる業務自動化を開始（RPA・BI・帳票処理） |
| 2025-03 | **MeaningSpace構想** — 「人間がAIの意味空間に入る」方向へ反転。減算設計を基本哲学に個人AI記憶OSの開発開始 |

## Era 2 — 意味記憶OSの確立
| 日付 | 出来事 |
|---|---|
| 2026-01-02 | **現行DuckDB結晶データベース稼働**（第1結晶） |
| 2026-05-16 | マルチエージェント企業OS構想を文書化 |
| 2026-06-04〜07 | QIS（Quantum Inspired Semantic Space）設計〜Phase 0+1実装（posi_vec/nega_vec全結晶バックフィル） |
| 2026-06-05〜07 | SubtractLabブランド確立・subtractlab.com公開（GitHub Pages） |
| 2026-06-11 | QIS干渉式 Model 2 確定（proximity主軸＋成功超過ボーナス／失敗超過ペナルティ） |
| 2026-06-13 | 結晶化の完全機械化 — 手動Raw方式撤去、会話ログ起点パイプラインへ一本化 |

## Era 3 — 司令塔と自己進化
| 日付 | 出来事 |
|---|---|
| 2026-07-04 | サブエージェント作法v2 — Chain / Swarm / Loop 3形態と昇格ラダーを体系化 |
| 2026-07-05〜 | Clara bridge — AI同士のファイルキュー対話ブリッジ設計・部分実装 |
| 2026-07-08 | **自己学習パイプライン実装**（SelfEval → EWMA → self_preferences → boot自動装着）。同日 **SelfRepair設計**（弱みスコア≤−3.0で改修Task自動起票）、司令塔構造欠陥4点修正、Loop体系化 |
| 2026-07-11 | self_preferences v8 稼働。API課金経路とWeb枠経路の費用構造を実測解剖 |

## Era 4 — DPマルチエージェント（Web Claudeを束ねる）
| 日付 | 出来事 |
|---|---|
| 2026-07-13 | **DPマルチエージェント基盤確定** — 5レーンCDP構成。同時実行上限・時差投入2.5s・ゾンビ応答と協調停止順序（3.6秒全停止実測）・人格汚染の中和ヘッダ・「触る係=Python/決める係=DP」分離・削除権限不付与。AutoCrystallize DPルート全8ステップ実証 |
| 2026-07-14 | **恒久化** — dp_lease（プロセス跨ぎスロット排他）、dp_journal（構造化ラン記録）、UI文字列判定全廃、dp_swarm量産基盤（Haiku一次→決定的検証→昇格ラダー、ベンチ4/4 PASS・9〜15秒/件・¥0）、COMMANDER_PLAYBOOK |
| 2026-07-15 | **能動的コーディングループ実戦投入** — checks検証 × dp_chat再依頼のEvaluator-OptimizerでF6動線フックv2をDPが実装。dp_swarm完成・応答洗浄恒久化。取扱説明書自体もDPが生成 |
| 2026-07-16 | **本タイムラインとアーキテクチャ全貌を公開**（[architecture.html](https://subtractlab.com/architecture.html) / [dp-multiagent.md](dp-multiagent.md)） |

## Era 5 — 意味の住所と、公開記録
| 日付 | 出来事 |
|---|---|
| 2026-09-01 | SweepSearch を退役 — 検索を一本化 — 言葉の検索（BM25）と意味の検索（ベクトル）を順位で合わせる検索に一本化。結果からは節へ降りて読む形にした。 |
| 2026-09 | 結晶の節ごとに、元の行への住所 — 会話の結晶の各節に、元の会話ログの行への住所を付けた。住所はモデルに思い出させず、決まった候補の中から選ばせる。 |
| 2026-09-21 | **作法を「灯らせて」引く道具** — 作法（手順）を、問いとの近さが閾値0.80を超えた時だけ、題名と読み方だけで返す道具を新設。検索結果への同梱はやめた。 |
| 2026-10-04 | **プログレスマップ — ファイルの地図と、理由付きの変更台帳** — ファイルとコードの「今」を地図にし、変更ごとに札・理由・逆向きの差分を台帳に積む。札は会話の記録に残り、見る時に会話の節へ結ぶ。git は使わない。 |
| 2026-10-07 | **設計をリポジトリとして公開（1〜2本目）** — [meaningspace](https://github.com/subtractlab/meaningspace) と [ai-native-groupware](https://github.com/subtractlab/ai-native-groupware) を、日付の入った設計の公開記録として公開。 |
| 2026-10-24 | 作法の一覧をプロンプトから外す — いつも読み込むプロフィールにあった25行の作法の一覧を外した。外す前に、25枚すべてが自分の仕事の問いで3位以内に灯ることを確かめた。 |
| 2026-11-07 | **設計の公開（3〜4本目）とトップページの作り直し** — [progress-map](https://github.com/subtractlab/progress-map) と [threshold-skills](https://github.com/subtractlab/threshold-skills) を公開。subtractlab.com のトップを、文字で読める HTML に作り直した。 |

---
*追記はコミット単位で日付が刻まれる。改竄不能性の根拠: git履歴・GitHub Pages配信記録・検索エンジンのインデックス日時。*
