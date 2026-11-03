---
name: quy-bi-ke-den-sau
description: Viết, biên tập, quản lý truyện đồng nhân Quỷ Bí Chi Chủ (Lord of the Mysteries), với nhân vật mới xuyên không cùng ngày Klein tỉnh ở Tingen, con đường Ẩn Giả, tri thức nguyên tác và kết nối Nguyên Bảo yếu. Dùng khi khởi tạo dự án, thiết kế arc, đối chiếu niên biểu canon/AU, viết chương, kiểm thử suy luận, kiểm soát tri thức nhân vật, hấp thụ ma dược, kiểm tra thay đổi lịch sử, phản biện và tạo arc tiếp theo.
---

# Kẻ Đến Sau — quy trình sáng tác đồng nhân cho Codex

## Nguyên tắc không thương lượng

1. **Canon phần 1 là mốc gốc, không phải đường ray bắt buộc.** Giữ các sự kiện lớn làm neo; các sai lệch nhỏ phải có nguyên nhân, nhật ký hậu quả và hệ số lan truyền. Không lấy phần 2 làm canon mặc định cho năm 1349.
2. **Người xuyên không không có toàn tri.** Phân biệt ký ức độc giả trước xuyên không, kiến thức đã xác minh trong thế giới mới, suy đoán, lời nói dối và bí mật của tác giả. Tránh khiến nhân vật nhận ra Quỷ Bí ngay trang 1.
3. **Chọn đường Ẩn Giả, bắt đầu người thường.** Vết sương mù xám che chắn *một phần* các lần truyền tri thức bị động nhưng không cấp quyền vào Nguyên Bảo, không thay thế ma dược, không miễn nhiễm ô nhiễm, có nguy cơ bị truy dấu. Đó là *giả định AU*, không được ghi là quy tắc canon.
4. **Không vào Hội Tarot giai đoạn đầu.** Hội Tarot tiếp tục sinh trưởng độc lập. Quanh mốc gia nhập Cattleya trong nguyên tác (~1/1350), tạo fork có nhân quả để OC thay Cattleya nhận lá Ẩn Giả; Cattleya vẫn có vai trò lớn. Sau đó Thế Giới và OC hợp tác ngày càng thường xuyên, tạo tình bạn thực sự. Klein tự điều tra thân phận cùng nguồn gốc của OC, KHÔNG được nhận trợ giúp từ OC cho cuộc điều tra đó. Đọc `references/tarot-and-world.md`.
4a. **Giữ sân khấu của Ngu Giả trong mọi buổi họp Tarot.** OC biết phần 1 nhưng phải giữ nguồn, mức chắc chắn và rủi ro. Không nói biết tuốt, không khoe identity Ngu Giả/Thế Giới, không giảng giải hay đính chính thay Ngu Giả. Klein có sáng kiến và uy nghiêm công khai, các thành viên khác có agency. Với từng buổi họp điền `continuity/tarot-meeting-ledger.json`. **BẮT BUỘC đọc `references/tarot-etiquette.md`.**
4b. **Chiến đấu và quan hệ phải khớp canon**: kiểm từng cấp Danh sách và ngày, ghi fight-card rồi mới viết; Hermit pathway khác với Sage Seq2. Đọc `references/combat-pairing.md` và `references/cattleya-bernadette.md`.
5. **Thăng cấp nhanh nhưng trả giá thật.** Phương pháp nhập vai, hiểu biết tiền đề, luyện tập và nguồn nguyên liệu kiểm chứng cho phép nhanh hơn người thường, không cho tự tăng cấp miễn phí.
6. **Không giả vờ tự động làm việc khi không có lượt chạy.** Chỉ thực hiện trong phiên Codex hiện hành. Tuyệt đối không push, không thêm remote, không cài package toàn cục, không sửa repo khác.
7. **Cổng duyệt:** trước khi người dùng trực tiếp duyệt Chương 001, không tạo Chương 002. Sau đó viết 2–4 chương mỗi lượt, QA và commit theo từng lô. Arc 2 cần duyệt riêng.
8. **Không sao chép lời văn gốc.** Chỉ dùng thiết lập/nhân vật được nhắc đến ở mức cần cho đồng nhân, tạo tình tiết và đoạn văn mới; đánh dấu đây là fanfiction phi thương mại và không ngụ ý liên kết tác giả gốc.

## Quy trình khi mới nhận ZIP

1. Đọc `README_FIRST.md` và `references/canon-au.md`.
2. Chạy `bash quy-bi-ke-den-sau/scripts/bootstrap.sh` từ thư mục chứa skill. Script dựng *thư mục mới* bên cạnh, tự chép skill vào `.agents/skills/quy-bi-ke-den-sau/`, `git init`, `git commit` local, không đè dữ liệu.
3. Đọc `AGENTS.md`, `bible/`, `arcs/arc-001/`, `continuity/` trong repo mới, kiểm tra `python3 .agents/skills/quy-bi-ke-den-sau/scripts/check_project.py .`.
4. Đánh giá và chỉnh sửa **chỉ** `chapters/001.md` trong phạm vi chưa duyệt, update báo cáo, kiểm tra và commit. Báo đường dẫn, SHA, bản review; ngừng.
5. Nếu người dùng duyệt bằng lời rõ ràng, làm quy trình phê duyệt theo `PROMPT_AFTER_APPROVAL.md`, khóa hash nội dung Chương 001 rồi mới viết tiếp.

## Khi viết chương mới

- Đọc `references/roles.md`, `references/scenario-design.md`, `references/continuity-and-qa.md`, `references/vietnamese-prose.md`, `references/nonrepeat-arc-design.md` khi có liên quan.
- Trước khi viết: kiểm tra `bible/canon-anchors.md`, `continuity/canon-log.md`, `continuity/character-knowledge.json`, hồ sơ giải đáp và chứng cứ (không lộ file giải đáp cho blind-reviewer).
- Tạo nhịp chương có mục đích: thay đổi thông tin, quan hệ, quyết định hoặc nguy cơ. Không rập khuôn cliffhanger.
- Sau khi viết: 1) kiểm tra canon và ngày; 2) kiểm tra kiến thức nhân vật; 3) kiểm tra ma dược/giá phải trả; 4) review văn; 5) cập nhật memory; 6) chạy script; 7) commit local.
- Arc sau bắt buộc có dấu vân tay (`continuity/arc-fingerprints.json`), khác arc trước về đối thủ, cơ chế, địa điểm, vấn đề đạo đức, cách giải và dư âm.

## Các tài liệu then chốt

- `references/canon-au.md`: nguồn và phân ranh canon/AU (mốc tháng 6–9/1349).
- `references/plot-architecture.md`: thiết kế phát hiện Quỷ Bí dần dần và 8 arc tiếp nối.
- `references/tarot-and-world.md`: điểm rẽ Cattleya, giao dịch tri thức, quan hệ Thế Giới–Ẩn Giả và điều tra độc lập của Klein.
- `references/tarot-etiquette.md`: nghi thức Hội Tarot, OC giấu sự toàn tri và để Ngu Giả duy trì uy quyền.
- `references/combat-pairing.md`: kỹ thuật phối hợp The World–Hermit đúng Danh sách và giới hạn.
- `references/cattleya-bernadette.md`: quan hệ Cattleya/Bernadette/Klein và các lần giao cắt có nhân quả.
- `references/acting-and-fog.md`: bảo hộ sương mù, cách tiêu hóa nhanh có điều kiện, rủi ro Ẩn Nặc Hiền Giả.
- `references/continuity-and-qa.md`: cổng duyệt + blind solvability.
- `assets/project_template/`: đầu vào tạo repo truyện gồm Chương 001 để đọc thử và outline 30 chương.
