# Vibe Story

Kho chứa nhiều dự án truyện độc lập. Mỗi truyện nằm trong một thư mục ở root, có tài liệu, chương, continuity và công cụ riêng.

| Truyện / gói truyện | Điểm bắt đầu | Trạng thái hiện có |
|---|---|---|
| Biên Bản Sai Lệch | [Đọc chương001–020](bien-ban-sai-lech/DOC_TRUYEN.md) · [README](bien-ban-sai-lech/README.md) | Đã viết/kiểm tra20chương; dừng tại020 chờ phản hồi, arc001 chưa khép |
| Quỷ Bí — Kẻ Đến Sau | [README_FIRST](quy-bi-ke-den-sau/README_FIRST.md) · [SKILL](quy-bi-ke-den-sau/SKILL.md) | Gói nguồn/khởi tạo được nhập nguyên trạng từ folder đã có; xem README_FIRST để sử dụng |

## Thêm truyện mới

Tạo hoặc chép một folder truyện mới cạnh hai folder trên, rồi thêm liên kết vào bảng. Chạy các kiểm tra riêng từ folder truyện đó; không dùng cổng duyệt hoặc continuity của truyện khác. Chỉ root repo này quản lý Git; không chép thư mục `.git` từ dự án con vào đây.

Các ghi chú tác giả trong `bible`, `arcs`, `continuity`, `long-game`, `reviews` hoặc template có thể tiết lộ diễn biến. Đọc truyện qua mục lục hoặc đường dẫn chương để tránh spoiler.

## Kiểm tra Biên Bản Sai Lệch

```bash
cd bien-ban-sai-lech
python3 .agents/skills/webnovel-studio/scripts/check_project.py .
```

Các folder nguồn ban đầu được giữ nguyên tại máy khi nhập kho; bản trong repo này là nơi lưu trữ Git chung cho nhiều truyện.
