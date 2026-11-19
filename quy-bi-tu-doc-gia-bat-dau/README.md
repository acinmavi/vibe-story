# Quỷ Bí: Từ Đọc Giả Bắt Đầu — dự án dịch tiếng Việt

- **Nguyên tác:** 诡秘：从阅读者开始 — 名火速返
- **Mục tiêu duy nhất:** dịch đầy đủ các chương có nguồn hợp lệ sang tiếng Việt tự nhiên, soát lỗi và xuất **một file EPUB tiếng Việt** khi hoàn tất.
- **Phong cách:** câu văn mượt, có nhịp tiểu thuyết; trung thành với hành động, tình tiết và đối thoại; không dịch máy thô, không tự thêm tình tiết.
- **Vùng làm việc:** nhánh `translation/quy-bi-doc-gia-20261106`. Không sửa hai dự án tiểu thuyết khác trong repo.
- **Tiến độ:** xem [PROGRESS.md](./PROGRESS.md).
- **Thuật ngữ:** xem [GLOSSARY.md](./GLOSSARY.md).
- **Chất lượng nguồn:** xem [SOURCE_GAPS.md](./SOURCE_GAPS.md).

## Cấu trúc

`chapters/0001.md`, `chapters/0002.md`, ...: **chỉ chứa bản dịch tiếng Việt thực sự đã hoàn thành**. Số chương tính theo thứ tự nguồn đã được đối chiếu, không dùng bản tóm tắt làm chương.

Khi đủ chương có nguồn xác minh, sẽ kiểm tra trùng/lặp/trật tự, thống nhất tên riêng và đóng một EPUB với mục lục đầy đủ.

## Quy trình mỗi lần tiếp tục

1. Kiểm tra trạng thái nhánh và file PROGRESS.md, đọc 2–3 chương đã dịch gần nhất để giữ văn phong.
2. Đối chiếu chương gốc do người dùng cung cấp; nếu thiếu/nhầm nguồn, ghi blocker, **không bịa**.
3. Dịch từng chương, tự soát sự kiện và thuật ngữ, commit riêng từng chương.
4. Cập nhật PROGRESS.md và các vấn đề cần giải quyết.
5. Khi dịch và kiểm tra **toàn bộ**, mới xuất EPUB cuối cùng.

**Quan trọng:** Không có tác vụ ngầm tự chạy sau khi phiên ChatGPT kết thúc. Mỗi lần người dùng yêu cầu tiếp tục, cần mở lại GitHub để tiếp tục từ trạng thái được commit.

## Quyền nội dung

Đây là dự án chuyển ngữ phục vụ đọc cá nhân từ dữ liệu người dùng cung cấp. Nguyên tác và các quyền liên quan thuộc về tác giả/chủ sở hữu; không mặc nhiên có quyền xuất bản, phân phối bản dịch hay gán giấy phép mới. Repository hiện đang công khai; cần kiểm tra quyền trước khi công bố rộng rãi. Không đưa bản TXT/HTML tiếng Trung đầy đủ vào repository công khai.
