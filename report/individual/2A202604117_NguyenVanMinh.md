# Báo cáo Day 7 — 2A202604117 · Nguyễn Văn Minh · L3B

## Dữ liệu và benchmark

- **Nguồn:** tái dùng nguyên kho Day 6 — 14 preprint arXiv (RL + điều khiển tối ưu), license CC BY 4.0, **264 trang nội dung** (text chuẩn hóa tại `day6/pages.jsonl`, manifest tại `day6/manifest.json`). Vector store **Qdrant embedded** (`day6/qdrant_data/`, collection `day6_chunks`) giữ nguyên **949 chunk** của chiến lược C Day 6 (paragraph ~1200 ký tự, page-scoped); chunk ID, nguồn, trang không đổi.
- **Embedding:** `BAAI/bge-small-en-v1.5` (384 chiều, ONNX local qua fastembed, query dùng `query_embed` đúng prefix retrieval) — đúng model/chiều của index Day 6, 0 USD. Xét `mistral-embed`/`codestral-embed` nhưng **không đổi**: đổi embedding bắt buộc tạo index mới (GUIDE §1), không cần cho mục tiêu bài.
- **Agent model:** Mistral API — `mistral-small-latest` (baseline + cấu hình cải thiện), `mistral-medium-latest`, và `mistral-large-latest` + `reasoning_effort=low` (cấu hình chọn cuối cùng; các mức thinking được probe thực nghiệm tại `starter/scripts/probe_thinking.py`: large hỗ trợ low/medium/high, medium chỉ high, small chỉ none, magistral none/high). Nhiệt độ 0, tool calling tự do trong giới hạn cấu hình.
- **Chia dev/test:** benchmark `benchmark/questions.jsonl` gồm **24 câu**: dev 15 câu có đáp án + 2 câu thiếu bằng chứng (u01, u02); test 5 câu có đáp án + 2 câu thiếu bằng chứng (u03, u04). 20 câu có đáp án giữ nguyên từ Day 6 (gold source/page/evidence, đã kiểm chứng evidence nằm trọn trong một chunk C; riêng q06 thu hẹp evidence về đoạn trong chunk abstract vì quote gốc vắt qua ranh giới paragraph — ghi rõ trong `starter/scripts/build_benchmark.py`). 4 câu thiếu bằng chứng viết mới, **gần chủ đề** (POMDP/Lipschitz/GPU/quadruped) và kiểm chứng vắng mặt bằng scan từ khóa toàn bộ 264 trang + đọc top-10 dense/BM25; cách kiểm tra ghi trong trường `verification` của từng câu.
- **Tiêu chí chấm:** hit = chunk đúng nguồn + đúng trang gold + chứa evidence (so khớp không phân biệt whitespace, cùng quy tắc Day 6). Grounded answer 0/1/2; citation hợp lệ = ID có trong context **và** đoạn được cite hỗ trợ câu trả lời (đọc thủ công); abstention đúng = câu thiếu bằng chứng bị từ chối. Câu thiếu bằng chứng không vào mẫu số metric retrieval. Gold không bao giờ vào agent, query hay filter.

## Retrieval và thử nghiệm

Ba phương pháp trên cùng corpus, cùng index C, cùng bộ dev (15 câu có đáp án), cùng cutoff top-3. BM25 dùng tokenizer từ đơn (corpus tiếng Anh; corpus tiếng Việt sẽ cần tách âm tiết/từ — ghi là giới hạn). Hybrid dùng RRF (k=60, không cần chuẩn hóa score cosine vs BM25). Không dùng filter ở tầng so sánh (các câu filter Day 6 giữ `filter` trong benchmark; agent không được cấp filter từ gold).

| Cấu hình | Phương pháp, top-k, budget | Giả thuyết / thay đổi | Split | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Thời gian / chi phí |
|---|---|---|---|---|---|---|---|
| Dense | dense, top-3, budget 800 | baseline: vector store Day 6 | dev | 8/15 (53%) | 11/15 (73%) | **1/15 (7%)** | 70 ms/câu, $0 |
| Phương pháp 2 | BM25, top-3, budget 800 | từ khóa bắt quote kiểu abstract tốt hơn embedding | dev | **11/15 (73%)** | **14/15 (93%)** | 1/15 (7%) | 4 ms/câu, $0 |
| Phương pháp 3 | Hybrid RRF, top-3, budget 800 | gộp hai xếp hạng, RRF không cần chuẩn hóa | dev | 10/15 (67%) | 12/15 (80%) | 1/15 (7%) | 76 ms/câu, $0 |
| Cải thiện 1a | dense, top-3, **budget 3500** | budget ≥ kích thước chunk thì evidence mới vào context | dev | 8/15 | 11/15 | 11/15 (73%) | 91 ms/câu, $0 |
| Cải thiện 1b | BM25, top-3, **budget 3500** | như trên | dev | 11/15 | 14/15 | **14/15 (93%)** | 4 ms/câu, $0 |
| Cải thiện 1c | hybrid, top-3, **budget 3500** | như trên | dev | 10/15 | 12/15 | 12/15 (80%) | 85 ms/câu, $0 |
| Cấu hình đã chọn | hybrid RRF, top-3, budget 3500 (agent: `hybrid3500`) | chọn theo tiêu chí dưới | test | 1/5 | 4/5 (80%) | 4/5 (80%) | 96 ms/câu, $0 |
| Baseline (tham chiếu) | dense, top-3, budget 800 | test sau khi chốt | test | 2/5 | 3/5 (60%) | 0/5 (0%) | 79 ms/câu, $0 |
| Baseline (tham chiếu) | dense, top-3, budget 3500 | tách ảnh hưởng budget khỏi phương pháp | test | 2/5 | 3/5 | 3/5 (60%) | 72 ms/câu, $0 |

Nhận xét: trên benchmark này BM25 mạnh hơn dense (câu hỏi phần lớn bám quote abstract), hybrid RRF nằm giữa vì xếp hạng dense yếu hơn làm loãng fusion. Vẫn chọn **hybrid** làm tool mặc định của agent vì (i) yêu cầu đề là dense phải có mặt và so sánh được, (ii) hybrid ổn trên cả hai kiểu câu (dense tốt với câu diễn đạt lại, BM25 tốt với thuật ngữ), (iii) agent có thể gọi thêm lượt tìm.

**Hai lỗi dev và cách xử lý:**

1. **Context budget 800 < kích thước chunk** (chunk C trung bình 838, tối đa 1317 ký tự): pack_context bỏ gần như mọi chunk → Context Evidence Rate 1/15 ở cả 3 phương pháp; agent baseline từ chối nhầm **7/15** câu có đáp án. Sửa: budget 3500 (~2-3 chunk nguyên vẹn) → CER dense 11/15, BM25 14/15, hybrid 12/15; agent `hybrid3500` từ chối nhầm 0/15.
2. **Citation không đọc được bằng máy** (trước structured output): model trả lời văn xuôi, nêu nguồn kiểu "(source, page)" thay vì `[chunk-id]` → kiểm tra citation cơ học fail → `alltools` abstain 11/17 dù tìm đúng evidence. Sửa: tách phase trả lời thành **một call structured output** (`response_format: json_schema` strict: `{enough_evidence, answer, citations[]}`), validate `citations ⊆ chunk đã gửi`. Kết quả trước/sau (cùng cấu hình): `alltools` 6→14 câu answered; `hybrid3500` 8→15.

Lỗi phụ (phân tích, không sửa bằng cấu hình): q09 model đọc bảng benchmark rồi tự tính "12x"/"17.8x" thay vì con số được báo cáo "8 times" (grade 0 với hybrid 1 tool); cấu hình nhiều tool/turn (`alltools`) tìm đúng chunk chứa "speeds up ... by 8 times (25 hours → 3 hours)" và trả lời đúng (grade 2) — bằng chứng nhiều lượt tìm giúp câu cần số liệu cụ thể.

**Tiêu chí chọn cấu hình (công bố trước khi chấm test):** (1) grounded answer mean /2 trên dev là chỉ số chính; (2) bắt buộc abstention 2/2 trên câu thiếu bằng chứng — bịa câu trả lời cho câu không có evidence là loại; (3) nếu chênh ≤ 0.2 (một bậc chấm của 1 câu) thì ưu tiên ít từ chối nhầm, rồi chi phí. Sau khi chạy test lần đầu với cấu hình chọn ban đầu (chỉ xem đếm status, chưa chấm nhãn), một thử nghiệm **chỉ trên dev** theo gợi ý về mức thinking (`mistral-large-latest`, `reasoning_effort=low`) đạt grounded dev cao nhất (1.87) → theo tiêu chí (1) trở thành cấu hình chọn cuối; test chạy lại cho cấu hình này. Test không dùng để chỉnh: quyết định hoàn toàn từ dev, và sau khi thấy test **không** đổi lựa chọn nữa (dù cấu hình chọn được 1.4 thấp hơn cấu hình ban đầu 1.6 — chênh 1 câu trong 5, trong biên độ nhiễu).

## Agent và đánh giá

- **Tool:** agent dùng model thật điều phối qua tool calling: `search_dense`, `search_bm25`, `search_hybrid` (mỗi tool nhận `query`, top-k theo cấu hình). Kết quả tool trả về dạng `[chunk-id | nguồn | page]\ntext`, dedup theo chunk đã gửi, gói trong budget ký tự. **Điều kiện dừng:** model hết gọi tool, hoặc chạm `max_tool_calls`/`max_turns` của cấu hình (không có giới hạn chung bắt buộc; các cấu hình 2–4 lượt). **Phase trả lời** là một call structured output riêng (json_schema strict) ép `{enough_evidence, answer, citations}`; citation phải là chunk đã thực sự gửi, nếu không → abstain. Nội dung chunk được coi là dữ liệu, không phải chỉ dẫn (ghi trong system prompt).
- **Xử lý lỗi:** lỗi API/mạng ghi `status: error` trong trace với nguyên nhân, **không** thay bằng kết quả giả; `agent_metrics.py` loại khỏi metric chất lượng và đếm `provider_errors` riêng. Retry 3 lần cho lỗi mạng/5xx/429. Trong các run đã nộp: 2 lần ConnectTimeout/ConnectionError (DNS WSL) — q19 ở `dense800-test` (giữ nguyên làm bằng chứng provider error) và q17 ở run test đầu của cấu hình chọn (chạy lại sạch, run lỗi vẫn lưu ở lịch sử local).
- **Tool use:** 17/17 câu dev và 7/7 câu test đều gọi retrieval tool. Phân bố lượt gọi: `dense800`/`hybrid3500` 1–2 lượt (mean 1.2–1.7), `alltools` 1–4 lượt (mean 3.1), large+thinking 2 lượt (mean 2.0).

| Cấu hình / split | Tool use | Số lượt gọi | Grounded answer 0/1/2 và trung bình | Citation hợp lệ | Câu có citation | Abstention đúng | Từ chối nhầm |
|---|---|---|---|---|---|---|---|
| dense800 (baseline) / dev | 17/17 | 1–2 | 8/2/5 → **0.80** | 7/9 | 8/8 | 2/2 | 7/15 |
| hybrid3500 (cải thiện 1) / dev | 17/17 | 1–2 | 2/1/12 → **1.67** | 18/23 | 15/15 | 2/2 | 0/15 |
| alltools (cải thiện 2) / dev | 17/17 | 1–4 | 2/2/11 → **1.60** | 20/24 | 14/14 | 2/2 | 1/15 |
| hybrid3500 + medium / dev | 17/17 | 1–2 | 2/0/13 → **1.73** | 19/25 | 15/15 | **1/2** (bịa u01) | 1/15 |
| alltools + medium / dev | 17/17 | 1–4 | 2/0/13 → **1.73** | 21/26 | 13/13 | 2/2 | 2/15 |
| hybrid3500 + large + thinking=low (cải thiện 3, **chọn**) / dev | 17/17 | 1–2 | 1/0/14 → **1.87** | 25/28 | 14/14 | 2/2 | 1/15 |
| dense800 (baseline) / test | 7/7 | 1–2 | 2/0/2 → **1.00** (N=4, 1 provider error) | 2/2 | 2/2 | 2/2 | 2/4 |
| hybrid3500 + large + thinking=low (**chọn**) / test | 7/7 | 1–2 | 1/1/3 → **1.40** | 7/7 | 4/4 | 2/2 | 1/5 |
| hybrid3500 + small (tham chiếu) / test | 7/7 | 1–2 | 0/2/3 → **1.60** | 9/11 | 5/5 | 2/2 | 0/5 |

**Context 0/1/2 trên test có đáp án** (baseline và cấu hình chọn, `starter/scripts/grade_context.py` + đọc lại tay): baseline `dense800`: 2 câu mức 2, 2 câu mức 0, 1 câu lỗi provider (không có context) — context hỏng vì budget 800. Cấu hình chọn: **5/5 câu mức 2** (đủ evidence + nguồn trong context cuối). Đáng chú ý: q19 test có evidence đầy đủ trong context nhưng model vẫn tự từ chối (false abstention) — lỗi "quá thận trọng" của phase structured, không phải lỗi retrieval.

**Nhãn chi tiết** (đầy đủ trong `results/agent/<run>/reviews.json` và `review_draft.md`, mỗi nhãn kèm lý do trong bảng dưới là bản rút gọn):

| Query ID | Loại câu | Tool call và kết quả | Câu trả lời và citation | Nhãn, lý do |
|---|---|---|---|---|
| q17 / test / chọn | có đáp án | 2 lượt hybrid, chunk gold `4f41f102` ở top-1 | "Upper Confidence Reinforcement Learning with several Modules" `[4f41f102]` | 2 — đúng và đủ, citation chứa gold evidence |
| u03 / test / chọn | thiếu bằng chứng | 2 lượt hybrid, chỉ chunk về AD4RL không ghi GPU | "Không đủ bằng chứng để trả lời." | abstention đúng — corpus không ghi hardware |
| u01 / dev / medium | thiếu bằng chứng | 2 lượt, chunk queueing networks | Bịa "Norton's theorem ... polynomial-time POMDP" | **abstention SAI** — medium gán khẳng định không có trong chunk; lý do loại cấu hình này |
| q09 / dev / chọn | có đáp án | 2 lượt hybrid, chỉ lấy được bảng benchmark | (abstain) | 0 — từ chối nhầm; evidence "8 times" nằm ở chunk khác, 2 lượt không đủ để tìm thấy |
| q09 / dev / alltools | có đáp án | 3 lượt (dense+bm25+hybrid) | "sped up by 8 times (25 hours → 3 hours)" `[ad8b0c36]` | 2 — citation chứa nguyên văn "speeds up ... by 8 times" |

- **Trace, nhãn, lệnh chạy:** mọi query lưu full trace (tool call, tham số, query, kết quả, context cuối, câu trả lời, citation, số lượt, thời gian, token) tại `results/agent/<run>/traces.jsonl` (+ `traces.json` cho script tổng hợp). Chi phí ước tính từ token thực tế, giá list giả định USD/1M: small 0.10/0.30, medium 0.40/2.00, large 2.00/6.00 (input/output; token thô ghi trong từng trace để quy đổi lại). Chi phí/run dev: small $0.0035–0.0083, medium $0.026–0.038, large+thinking $0.134. Run test: baseline $0.0012, cấu hình chọn $0.052.
- **Trước/sau, đánh đổi, giới hạn:** hai lỗi dev đã nêu có đo trước/sau rõ ràng (budget: false abstention 7→0; structured output: answered 6→14). Đánh đổi chính: large+thinking +0.2 grounded so với small nhưng **25× chi phí** và ~2× thời gian (median 14.1s vs 7.7s/câu); medium nhanh nhất (2.9s) nhưng bịa bằng chứng trên câu thiếu evidence → loại. Giới hạn: (i) test chỉ 5 câu có đáp án nên chênh 1.4 vs 1.6 là nhiễu; (ii) hit dựa trên evidence substring nên paraphrase hợp lệ có thể bị đếm là miss; (iii) benchmark thiên về quote abstract nên BM25 được lợi bất công so với dense; (iv) nhãn chấm do người + AI hỗ trợ soạn, từng nhãn đã đối chiếu text chunk đầy đủ (không chỉ ID).

## Tái lập

```bash
python3 -m venv .venv && .venv/bin/pip install -r starter/requirements.txt
cp .env.example .env   # điền MISTRAL_API_KEY (file .env bị git-ignore)

python starter/scripts/build_benchmark.py        # tạo benchmark/questions.jsonl (24 câu)
python starter/scripts/verify_unanswerable.py    # kiểm chứng 4 câu thiếu bằng chứng
python starter/scripts/run_retrieval_bench.py --method dense  --split dev --top-k 3 --budget 800  --output results/retrieval/dense-dev
python starter/scripts/run_retrieval_bench.py --method bm25    --split dev --top-k 3 --budget 800  --output results/retrieval/bm25-dev
python starter/scripts/run_retrieval_bench.py --method hybrid_rrf --split dev --top-k 3 --budget 800 --output results/retrieval/hybrid_rrf-dev
python starter/scripts/run_agent_bench.py --config dense800  --split dev --output results/agent/dense800-dev
python starter/scripts/run_agent_bench.py --config hybrid3500 --split dev --output results/agent/hybrid3500-dev
python starter/scripts/run_agent_bench.py --config alltools   --split dev --output results/agent/alltools-dev
python starter/scripts/run_agent_bench.py --config hybrid3500 --split dev --model mistral-medium-latest --output results/agent/hybrid3500-medium-dev
python starter/scripts/run_agent_bench.py --config alltools    --split dev --model mistral-medium-latest --output results/agent/alltools-medium-dev
python starter/scripts/run_agent_bench.py --config hybrid3500 --split dev --model mistral-large-latest --reasoning-effort low --output results/agent/hybrid3500-large-low-dev
# sau khi chốt cấu hình trên dev:
python starter/scripts/run_agent_bench.py --config dense800  --split test --output results/agent/dense800-test
python starter/scripts/run_agent_bench.py --config hybrid3500 --split test --model mistral-large-latest --reasoning-effort low --output results/agent/hybrid3500-large-low-test
# soạn hồ sơ chấm + ghi nhãn + tổng hợp:
python starter/scripts/draft_reviews.py --traces results/agent/<run>/traces.jsonl --output-dir results/agent/<run>
python starter/scripts/apply_reviews.py --run <run> --run-dir results/agent/<run>
python starter/agent_metrics.py --cases results/agent/<run>/cases.json --traces results/agent/<run>/traces.json --reviews results/agent/<run>/reviews.json --split dev --output results/agent/<run>/summary_metrics.json
python starter/scripts/grade_context.py --traces results/agent/<run>/traces.jsonl --run <run>
python -m unittest discover -s tests -v
```

Embedding chạy local (ONNX, không cần key ngoài Mistral cho agent). `day6/qdrant_data` đã commit để chấm lại offline; tái tạo từ đầu bằng pipeline Day 6 nếu cần.

## Thử thách nâng cao (nếu thực hiện)

Không thực hiện trong lần nộp này — phần cơ bản đã dùng toàn bộ thời gian lab cho 3 phương pháp retrieval, 6 cấu hình agent và phân tích lỗi. Hướng làm nếu tiếp tục: index một sách/report 100+ trang có bảng/biểu đồ bằng pipeline Day 6 mở rộng (OCR bảng bằng `mistral-ocr`, chart caption làm metadata), benchmark riêng theo nhóm nội dung theo ADVANCED.md.
