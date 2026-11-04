# Prompt cho Codex sau khi người dùng duyệt

Nhận đúng lời duyệt công khai từ người dùng. Nếu người dùng yêu cầu sửa thì sửa CHƯƠNG 001, QA và gửi lại, KHÔNG mở khóa.

Nếu người dùng viết rõ 'Tôi duyệt Chương 001, hãy viết tiếp Arc 1':
1. Lưu lời duyệt đầy đủ trong `approvals/approval.json` trường `chapter1.approval_text` và `arc001_writing.approval_text`.
2. Đặt `approved_at_utc` là thời điểm hiện tại thực tế và `approved_sha256` bằng sha256 của `chapters/001.md`.
3. Đặt `stage` và `continuity/story-state.json` `phase` là `arc1_writing`, `do_not_write_after_chapter=30`.
4. Ghi commit mở cổng duyệt.
5. Viết chương 2–30 theo lô 2–4, mỗi chương 1800–3000 từ khi hoàn thiện; cập nhật `last_written_chapter`, `character-knowledge`, `open-loops`, canon-log, QA. Chỉ xuất bản file nếu QA đạt.
6. Kiểm tra thường xuyên ngày, công thức/nguyên liệu và phương pháp nhập vai; không đẩy nhân vật nhanh hơn Klein vô cớ.
7. Commit từng lô local, không push, không remote. Nếu thiếu thời gian/quota của phiên, báo những gì đã hoàn thành; không tuyên bố đã viết những chương chưa có.
8. Sau arc1, chờ duyệt arc2 riêng.
