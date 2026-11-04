# Biên tập nhịp kể, xác minh thời gian và công việc của Evan

Bạn nên đọc lại từ **chương002**; chương001 giữ nguyên. Nếu muốn xem ngay phần thay đổi lớn nhất, đọc004–008. Hai bản đọc liền [Arc1](../../ARC_001.md) và [Arc2](../../ARC_002.md) đã đồng bộ.

## Nguyên nhân bản cũ chậm và khó theo dõi

Bản cũ áp dụng sự thận trọng quá đều: một việc đời thường cũng được kiểm nhiều nguồn, rồi nhắc lại điều chưa thể kết luận. Phần kiểm giấy tờ, xin quyền xem và tự giới hạn suy luận xuất hiện dày hơn mục đích nhân vật theo đuổi. Vì thế, độc giả dễ mất dấu Evan đang cần biết gì và vì sao điều đó quan trọng.

Đây là vấn đề cách kể và phân bổ thông tin, không phải yêu cầu của thiết lập rằng ngày tháng ở thế giới này không đáng tin. “Ba hòm” vẫn là vụ việc ban đầu khiến Evan phải chịu trách nhiệm trên phiếu hàng; nó không đòi hỏi anh liên tục hỏi lại cùng một câu khi không có thông tin mới.

## Những thay đổi chính — không tiết lộ sau008

- **002–003:** nói rõ Evan là thợ phụ xưởng in: so lỗi bản in, xếp giấy và phụ đóng sách. Chép phiếu, nhận hàng dưới kho là phần việc thêm. Mỗi đoạn thao tác được đặt sau mục đích công việc.
- **004:** xác nhận ngày30/6/1349 bằng lịch và người phụ việc đã thay lịch sáng ấy; không dựng thêm vòng xác minh hiện tại.
- **005:** đầu chương nêu mồng một tháng bảy. Báo cũ giúp nhận ra thế giới qua tên người và địa danh; ngày in trên báo không bị dùng thay ngày hiện tại. Giữ giới hạn giữa tin công khai và ký ức đọc truyện.
- **006:** câu hỏi tập trung vào ai đã dùng tên Evan và ai thực sự chứng kiến từng phần của lần nhận hàng. Giữ rõ người nào không thấy dỡ hàng; không biến lời nhớ lại thành chứng cứ chắc chắn.
- **007:** bỏ các lượt tìm thêm nguồn xác minh ngày đã biết. Mối bận tâm chuyển sang thời gian, tiền và lựa chọn trước mắt. Giữ giới hạn hiểu biết về Klein, sự e dè khi báo tin và trách nhiệm báo ngay nếu có người gặp nguy hiểm.
- **008:** bớt đếm và kiểm túi lặp; giữ toàn bộ khoản trả nợ, tiền còn lại, quan hệ với Mara và bà Finch. Cuối chương nối việc giúp Theo với tuyến hàng hóa đang theo đuổi.
- **009–068:** rà từng chương, gộp thao tác lặp và những đoạn nhắc lại giới hạn đã rõ; giữ các lần thất bại, điều kiện tiếp cận nguồn, chi phí, thương tích và quyền quyết định của nhân vật khác. Những câu ngắn có nhịp căng thẳng vẫn được giữ.

## Thống kê bản cuối

Đếm theo khoảng trắng (`split()`), không phải đơn vị từ vựng tiếng Việt:

| Phạm vi | Trước | Sau | Chênh lệch |
|---|---:|---:|---:|
| Arc1,001–030 | 64.387 | 51.236 | −13.151 |
| Arc2,031–068 | 71.016 | 61.845 | −9.171 |
| Toàn bộ | 135.403 | 113.081 | −22.322 (16,5%) |

67 chương có sửa;001 không đổi. Không đặt mục tiêu cắt theo tỷ lệ và không thêm chữ để bù độ dài. [Số từ và SHA256 từng chương](chapter-counts.csv) là bản cuối; số trong báo cáo làm việc bên dưới có thể thuộc thời điểm trước các chỉnh sửa QA cuối.

## Đối chiếu và giới hạn

Đã đối chiếu bản trước/sau từng nhóm chương, rà riêng mạch004–008 và các điều kiện quan trọng ở cuối hai arc. Những chỗ có nguy cơ lệch nội dung đã được sửa: không gán Evan biết sớm cách nguyên chủ xin việc; không tự thêm lỗi đối thoại hay sự cố vấp ghế; không nâng quyền xem tài liệu thành quyền công khai; không gọi một nhãn cũ là nhãn sai trước khi kiểm; giữ đúng người xác nhận và nguồn giấy tờ.

Chương001 và approval giữ nguyên byte. Không thêm069, không mở quyền Arc3, không nâng năng lực hay sửa trạng thái kết arc. Sự kiện chính, manh mối, lịch và tiền được kiểm về ý nghĩa; không dùng việc giữ nguyên mọi câu thoại hay con số xuất hiện trong văn làm chứng minh, vì yêu cầu mới cho phép bỏ những lượt kể lặp.

QA tự động của project PASS; kiểm khoảng trắng Git và đối chiếu bản đọc liền được thực hiện sau khi đóng bản. Script chỉ kiểm cấu trúc và các ràng buộc có thể đo; phần bảo toàn ý nghĩa dựa vào đối chiếu biên tập. Đây là sửa nhịp kể theo yêu cầu mới, không phải bản polish chỉ thay câu chữ trước đây.

## Hồ sơ chi tiết — có spoiler tới068

Các báo cáo làm việc được lưu trong [technical](technical/). Chỉ mở sau khi đọc tới chương tương ứng. Bản trước sửa có thể truy từ commit `179f9ffd23aa4c0d146ae3738d9f17b4c5934486`; bản thử003.polished.md và các báo cáo polish cũ là hồ sơ lịch sử.

Thay đổi nằm trên nhánh `edit/quy-bi-pacing-and-work-clarity`; chỉ commit local, không push hoặc merge trong nhiệm vụ này.
