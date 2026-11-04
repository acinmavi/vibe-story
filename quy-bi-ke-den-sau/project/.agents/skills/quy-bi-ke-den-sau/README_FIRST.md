# ĐỌC ĐẦU TIÊN — Codex, truyện đồng nhân Quỷ Bí Chi Chủ: Kẻ Đến Sau

Gói này là một **Codex skill tự chứa** và bản mẫu dự án đồng nhân. Đã có chương 1 (bản thảo cần độc giả thẩm), Arc 1 outline 30 chương, hồ sơ năng lực và cổng duyệt. Chưa viết chương 2–30.

## Dùng với Codex Desktop / CLI

Giải nén `skill.zip` vào một thư mục bất kỳ. Mở thư mục chứa `quy-bi-ke-den-sau` bằng Codex, rồi gửi:

> Đọc `quy-bi-ke-den-sau/README_FIRST.md` và `quy-bi-ke-den-sau/SKILL.md`. Tự chạy `bash quy-bi-ke-den-sau/scripts/bootstrap.sh` để tạo thư mục project mới, cài skill cục bộ, init local Git, commit và chạy QA. Đọc `AGENTS.md`, `bible`, hồ sơ Arc 1; rà soát và cải thiện chương 001 nếu thật cần, không tự đổi tiền đề. Tạo báo cáo review, chạy QA, commit local và báo đường dẫn cùng SHA. TUYỆT ĐỐI dừng trước chương 002 đến khi tôi duyệt chương 001.

Mặc định project mới ở thư mục `quy-bi-ke-den-sau` cạnh thư mục skill. Nếu trùng tên hoặc đã tồn tại, script **từ chối**, không ghi đè. Muốn đổi vị trí: `bash quy-bi-ke-den-sau/scripts/bootstrap.sh /duong/dan/thu-muc-moi`.

## Mốc canon cần giữ

- 28/06/1349: Klein (Chu Minh Thụy) thức tỉnh ở Tingen, lập Hội Tarot với Audrey, Alger trong ngày. Nhân vật phụ AU cũng tỉnh ngày này nhưng không biết tên thành phố hay thế giới ngay.
- 02/07/1349: Klein dùng ma dược Nhà Bói Toán.
- 29/08/1349: Old Neil mất kiểm soát và chết (mốc canon nhạy cảm; nếu thay đổi phải viết hệ quả lớn).
- 31/08/1349: Klein lên Danh sách 8 Hề.
- Tháng 9/1349: bi kịch Tingen; trong Arc 1 chưa sửa sự kiện này.
- Quanh 1/1350 (mốc tham khảo nguyên tác chương 564–566): tạo fork có nhân quả để MC gia nhập Hội Tarot nhận lá Ẩn Giả thay Cattleya. Quan hệ với Thế Giới dần sâu sắc; Klein độc lập điều tra chiếc kén thứ tư, chỉ chứng thực sau này khi đủ quyền tiếp cận Nguyên Bảo.

Các mốc tham khảo: https://lordofthemysteries.fandom.com/wiki/Volume_1%3A_Clown và https://lordofthemysteries.fandom.com/wiki/Old_Neil . Fandom là nguồn cộng đồng; Codex nên đối chiếu chương nguyên tác hợp pháp nếu có truy cập.

## Cổng duyệt và Git

- `approvals/approval.json`: mặc định chưa duyệt.
- `chapters/001.md`: chương mẫu đang chờ đọc.
- `PROMPT_AFTER_APPROVAL.md`: workflow sau khi nhận chữ 'duyệt'.
- Không tạo `chapters/002.md`, kể cả dưới tên khác, khi chưa có chỉ thị duyệt trực tiếp.
- Không push/remote/GitHub, không cài dependencies ngoài, không sửa thư mục của người dùng đã tồn tại.
- `python3 .agents/skills/quy-bi-ke-den-sau/scripts/check_project.py .` để kiểm tra trạng thái.

**Fanfiction phi thương mại; không liên quan đến hay được tác giả gốc chứng thực.** Không đưa văn bản nguồn truyện gốc vào repo.

## Cập nhật thiết kế tuyến Tarot và chiến đấu
- Khi OC nhận lá Ẩn Giả, **không được tỏ ra biết tuốt hoặc làm Ngu Giả mất sân khấu trong cuộc họp**; dùng `references/tarot-etiquette.md` và sổ Tarot meeting ledger.
- Trước trận phối hợp Thế Giới–Ẩn Giả phải khớp cấp Danh sách, vật phẩm, rủi ro: `references/combat-pairing.md`.
- Cattleya và Bernadette vẫn có những tuyến phát triển và liên hệ với Klein riêng: `references/cattleya-bernadette.md`.
