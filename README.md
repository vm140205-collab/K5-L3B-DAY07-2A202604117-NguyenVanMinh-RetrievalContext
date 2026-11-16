# Day 7 — Agentic RAG

## Bài làm: Nguyễn Văn Minh · 2A202604117 · L3B

**Báo cáo đầy đủ:** [report/individual/2A202604117_NguyenVanMinh.md](report/individual/2A202604117_NguyenVanMinh.md)

Tái dùng nguyên kho Day 6 (14 preprint arXiv, 264 trang, CC BY 4.0; 949 chunk chiến lược C trong Qdrant embedded; embedding `BAAI/bge-small-en-v1.5` 384 chiều, local ONNX, 0 USD). Agent dùng Mistral API với tool calling (dense / BM25 / hybrid-RRF) và phase trả lời **structured output** (`json_schema` strict) ép citation dạng `{enough_evidence, answer, citations[]}`; citation phải là chunk đã thực sự gửi tới model.

Benchmark 24 câu: dev 15 có đáp án + 2 thiếu bằng chứng; test 5 + 2 (4 câu thiếu bằng chứng viết mới, kiểm chứng vắng mặt bằng scan toàn corpus + đọc top-10 retrieval; cách kiểm tra ghi trong `verification` của từng câu).

| Cấu hình (dev, 15 câu có đáp án) | Grounded /2 | Abstention | Từ chối nhầm | Chi phí/run |
|---|---|---|---|---|
| Baseline dense800 (budget 800) | 0.80 | 2/2 | 7/15 | $0.0035 |
| hybrid3500 (budget 3500) | 1.67 | 2/2 | 0/15 | $0.0054 |
| alltools (3 tool, top-5) | 1.60 | 2/2 | 1/15 | $0.0083 |
| hybrid3500 + medium | 1.73 | **1/2** (bịa u01) | 1/15 | $0.026 |
| alltools + medium | 1.73 | 2/2 | 2/15 | $0.038 |
| **hybrid3500 + large + thinking=low (chọn)** | **1.87** | 2/2 | 1/15 | $0.134 |

Test (chốt cấu hình trên dev, không chỉnh sau khi xem test): cấu hình chọn grounded 1.40 (5/5 câu có context đủ evidence + nguồn, citation 7/7 hợp lệ, abstention 2/2); baseline 1.00. Chi tiết, trace, nhãn và phân tích lỗi trong báo cáo.

---

**Bài cá nhân · Python 3.11+ · tiếp nối Day 6**

Dùng embedding và vector store từ Day 6 để xây một agent biết tìm bằng chứng, trả lời có nguồn và nhận biết khi không đủ thông tin. Bạn tự chọn kiến trúc, số tool và cách tổ chức retrieval.

> **Tùy chọn:** [Gợi ý dùng AI để lập trình](AGENT_SETUP.md) giúp bạn làm lab; phần này không bắt buộc và không tính điểm.

## Bài cần làm

![Agent tìm tài liệu trong kho Day 6 và trả lời có nguồn](assets/retrieval-pipeline.svg)

1. Kết nối dữ liệu, embedding và vector store Day 6.
2. Xây agent dùng model thật và ít nhất một khả năng truy xuất dữ liệu. Agent có thể dùng nhiều tool và nhiều lượt gọi.
3. Thử **ít nhất 3 phương pháp retrieval khác nhau**, trong đó có dense retrieval dùng vector store Day 6. Tự chọn các phương pháp còn lại; xem [gợi ý](GUIDE.md#2-thử-các-phương-pháp-retrieval).
4. Thử nhiều cấu hình, benchmark, phân tích lỗi và chọn cấu hình tốt trên **dev**; sau đó đánh giá trên **test**.

Benchmark tối thiểu có **24 câu**: dev gồm 15 câu có đáp án và 2 câu thiếu bằng chứng; test gồm 5 câu có đáp án và 2 câu thiếu bằng chứng. Xem [benchmark](BENCHMARK.md) và [rubric](RUBRIC.md).

## Thử thách nâng cao · +15 điểm

Index một tài liệu thực tế từ **100 trang** có bảng, ảnh và biểu đồ; xây agent truy xuất và trả lời các câu hỏi về nội dung đó. Hoàn thành [thử thách nâng cao](ADVANCED.md) và đạt **ít nhất 90% benchmark test** để nhận 15 điểm bonus. Phần cơ bản tối đa 85 điểm; toàn bài tối đa 100 điểm.

## Bắt đầu

1. Đọc [hướng dẫn](GUIDE.md), [rubric](RUBRIC.md) và [quy tắc](RULES.md).
2. Tạo repo cá nhân theo [cách nộp bài](SUBMISSION.md), chuẩn bị đầu ra Day 6 và model hỗ trợ tool calling.
3. Dùng hoặc thay thế [starter](starter/README.md); bạn cần kết nối model và vector store thật.
4. Chạy `python -m unittest discover -s tests -v`. Test mock chỉ kiểm tra code, không phải benchmark agent thật.

![Các bước thử nghiệm trên dev và đánh giá trên test](assets/experiment-loop.svg)

Nộp code, cách chạy, cấu hình, benchmark, trace và [báo cáo](report/individual/MSSV_HoTen.md). Thời gian ở [checkpoints](CHECKPOINTS.md) là gợi ý, có thể điều chỉnh theo lớp và phạm vi thử nghiệm.
