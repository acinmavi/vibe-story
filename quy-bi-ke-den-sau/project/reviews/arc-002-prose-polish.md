# Báo cáo biên tập văn phong Arc 2 — 031–068

Ngày 04/11/2026. Nhánh `edit/prose-polish-arc1`. Nguồn so sánh: commit `8e838312e8c5560d00e637a4feaf08613f67989c`.

Người dùng duyệt bản thử003 và STYLE_GUIDE, cho phép sửa toàn bộ Arc1 gồm001 đã khóa, rồi yêu cầu tiếp Arc2. Không viết thêm chương, không push/merge; không đổi trạng thái duyệt arc.

## Phương pháp và phạm vi QA

Đọc trọn từng chương và phần nối, chọn chuỗi câu rời có cùng trọng tâm. Giữ lời thoại, khoảng ngắt nghệ thuật, điểm nhìn, mức chắc chắn, nguồn và vị trí vật chứng. Đề xuất được soát semantic trước khi áp dụng; loại mọi chỗ có thể thêm tác nhân, mục đích, vị trí hoặc độ chắc chắn. Không thêm cảnh hoặc làm dài để đạt chỉ tiêu từ.

Số từ đếm bằng split(), gồm tiêu đề; đoạn là khối cách bởi dòng trắng, không tính tiêu đề. Mỗi chương có kiểm máy riêng: tiêu đề, nguyên chuỗi chữ số, nguyên toàn bộ trích dẫn kép/đơn theo thứ tự, biến động độ dài. Script dự án kiểm cấu trúc và cổng duyệt; máy không tự chứng minh tương đương ngữ nghĩa hoặc chất lượng văn.

## Đối chiếu từng chương

| Chương | Từ trước → sau | Đoạn trước → sau | Trọng điểm bảo toàn |
|---|---:|---:|---|
| 031 | 1801 → 1803 | 96 → 95 | Giữ riêng chìa Gideon và chìa số sáu; không thêm quyền mở ngăn.; Giữ tiền 27+18−36−1=8 penny, đau tay phải, Mara tự chọn ở lại. |
| 032 | 1848 → 1846 | 82 → 82 | Ba lần nhắc địa chỉ vẫn chỉ một nguồn; Agnes có thẩm quyền giới hạn.; Không nhận diện khách hỏi nghề thành Kestrel; gốc bản vẽ giao Ruth, chỉ giữ sao; không biến lời thì thầm thành chứng cứ. |
| 033 | 1906 → 1906 | 83 → 83 | 8£ gồm ứng1£, vé/phòng trả trực tiếp; nợ132£ và ba nghiên cứu riêng giữ nguyên.; Quyền dừng/phạm vi công việc, ngày3/8 và custody gốc Ruth/chìa đã trả không đổi. |
| 034 | 1813 → 1814 | 68 → 68 | Cảnh đóng cửa chỉ quan sát khối thấp/nẹp đồng, chưa biết vòng.; Giữ Seq9/tay phải đau, kỹ thuật thuộc Nell, công/phòng và chi4p còn235p. |
| 035 | 1835 → 1838 | 76 → 76 | Giữ lỗi Evan nhầm hai lần ghi thành hai bản; không chuyển nghề đo/tải của Nell.; Mẩu nhắn chỉ được Nell đọc, chưa lộ chữ cho Evan; tiền232p/nợ132£ không đổi. |

Đã đối chiếu 5/38 chương thuộc arc. Bản gốc nằm trong Git tại commit nguồn; không xóa hoặc viết đè lịch sử.
