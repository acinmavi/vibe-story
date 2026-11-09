# Các vấn đề nguồn cần giải quyết trước khi hoàn thiện EPUB

Nguồn: `341776.zip` (TXT Ai Xia) và 7 file HTML do người dùng cung cấp trong hội thoại 2026-11-06.

## Đã xử lý trong bản dữ liệu phiên trước

- Chương **问答（补昨天的）** — tương ứng số 393 trong quyển Động Tất Giả.
- Chương **第二次茶话会** — chương 160 trong quyển Tháp.
- Chương **女武神** — chương 161 trong quyển Tháp.

## Còn thiếu hoặc không thể tin cậy

1. Hai file HTML mang nhãn **“愚者”苏醒前的塔罗会（中）** và **（下）** có nội dung trùng gần như hoàn toàn. Hai trang Piāotiān cũng lặp phần mở đầu. Qidian có hai mục VIP riêng nhưng chưa đọc được toàn văn để xác nhận bản nào khớp HTML hiện có. [Qidian, phần giữa](https://www.qidian.com/chapter/1026292682/746384906/) · [Qidian, phần cuối](https://www.qidian.com/chapter/1026292682/746578378/)
2. Đoạn cuối TXT tải từ Ai Xia có văn bản nhiễu/hỏng, gồm các đoạn từ tác phẩm khác; không đưa đoạn đó vào bản dịch cuối nếu chưa xác minh lại.
3. Các ngoại truyện cuối như **“愚者”的生日礼物** và **走向星空（完）** đã có HTML lưu lại, nhưng tổng thể phần phụ lục vẫn cần kiểm tra đối chiếu trước khi chốt.
4. Chưa có đối chiếu toàn văn 1.500+ chương so với bản chính thức. Không thể đảm bảo dữ liệu gốc đầy đủ chỉ nhờ số lượng mục lục.

## Chỗ nhảy số đã đối chiếu

- **0129, quyển Học Giả Uyên Bác.** Mục lục WebNovel ghi hai mục liền kề có tiêu đề chương 128 (`总结“守知者”扮演守则`) và chương 130 (`魔女的目的`). ZIP gốc và JSONL có cùng thứ tự. Mạch truyện nối tiếp từ đoạn Abner nghĩ đến việc mượn tiền Danitz ở cuối 128. Một số bản sao đánh số `魔女的目的` là 129. Giữ `0130.md` theo tiêu đề chính thức và bỏ qua số 0129 khi kiểm tra tính liên tục. [Mục lục WebNovel](https://www.webnovel.com/zh/book/19293266101452704/catalog) · [Mục lục bản đánh số lại](https://hetushu.com/book/7425/index.html)
- **0280, quyển Học Giả Uyên Bác.** TXT có đầy đủ mục `第280挖坟` giữa chương 279 và 281. Tiêu đề thiếu chữ `章` trong cả TXT và mục lục WebNovel, nên cần nhận diện theo tên và vị trí khi tách nguồn. [Mục lục WebNovel](https://www.webnovel.com/zh/book/19293266101452704/catalog)

**Không đặt chương trống, không bịa tình tiết, không thay chương không dịch bằng nguyên văn tiếng Trung rồi gọi là EPUB tiếng Việt hoàn chỉnh.**

## Lưu ý về quyền

Repository hiện **public**. Không mặc định quyền đăng tải công khai trọn bản dịch chỉ vì có file tải về; cần xác minh quyền xuất bản/phân phối trước khi phát hành toàn bộ. Giữ dữ liệu thô không công bố.

5. **Chương 0328, quyển Động Tất Giả — nguồn được cung cấp bị hỏng.** Trong cả `341776.zip` và `quy_bi_doc_gia_du_an_dich_epub.zip`, nội dung 0328 chỉ còn 10 đoạn / 326 ký tự, chủ yếu là thông báo lỗi và quảng cáo. Có trang Piāotiān trùng tên chương và mạch truyện: https://www.piaotia.com/html/14/14721/9908399.html. ChatGPT web xác minh trang có nội dung đầy đủ hơn nhưng không dùng văn bản lấy từ trang bên thứ ba để dịch nguyên chương. Để tiếp tục tuần tự, cần người dùng tải trang thành HTML/TXT và cung cấp trong `original/BQCC_Start_reader` hoặc đính kèm vào chat. Không dịch từ phần cụt, không bỏ qua chương.
