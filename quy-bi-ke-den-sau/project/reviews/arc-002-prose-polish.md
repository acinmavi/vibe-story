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
| 033 | 1906 → 1904 | 83 → 83 | 8£ gồm ứng1£, vé/phòng trả trực tiếp; nợ132£ và ba nghiên cứu riêng giữ nguyên.; Quyền dừng/phạm vi công việc, ngày3/8 và custody gốc Ruth/chìa đã trả không đổi. |
| 034 | 1813 → 1814 | 68 → 68 | Cảnh đóng cửa chỉ quan sát khối thấp/nẹp đồng, chưa biết vòng.; Giữ Seq9/tay phải đau, kỹ thuật thuộc Nell, công/phòng và chi4p còn235p. |
| 035 | 1835 → 1838 | 76 → 76 | Giữ lỗi Evan nhầm hai lần ghi thành hai bản; không chuyển nghề đo/tải của Nell.; Mẩu nhắn chỉ được Nell đọc, chưa lộ chữ cho Evan; tiền232p/nợ132£ không đổi. |
| 036 | 1847 → 1858 | 82 → 82 | Hai suất/hai bát/hai thìa và chai rửa vết thương không xác nhận Edith ở trong hoặc bị thương.; Giữ lần gặp1/8, vắng hai tối, báo tìm người5/8 và hẹn tuần tra trong ngày. |
| 037 | 1863 → 1864 | 62 → 62 | Pike/giờ nhận xe và giờ giao hòm tách biệt; không đồng nhất người áo sẫm.; Phấn trắng chỉ giải thích phù hợp nghề, không giám định; ca thêm và chữ phù hợp không chứng minh âm mưu/xuyên không. |
| 038 | 1809 → 1814 | 60 → 60 | Đo12foot6inch/vạch A và hai cách đo giữ nguyên; chưa được thử người.; Dấu bùn chưa xác định chủ/quay ở đâu; Nell/thợ giữ quyền kiểm sàn, không biến Evan thành kỹ sư. |
| 039 | 1805 → 1811 | 60 → 60 | Không dùng người nhẹ hơn để thử tải; phép thử vật bị lệch không được dùng kết quả.; Ván mở/thanh đỡ hụt/nhánh cơ cấu sau lưới và mối kê trượt giữ riêng; không suy sức chịu tải chung. |
| 040 | 1860 → 1862 | 85 → 85 | Jonah/Edith tự nguyện vẫn chỉ lời Silas; không thêm xác nhận trực tiếp.; Động tác Silas không xác định Danh sách; chốt/khối hạ cuối ca giữ nguyên; hẹn sáng7/8 và quyền báo khẩn không mất. |
| 041 | 1867 → 1868 | 48 → 48 | Linh thị chỉ nhịp thứ ba đau rồi thu ngay, vệt mờ chưa xác định; không thêm mức tiêu hóa/năng lực.; Jonah chưa gặp/chưa nghe/chưa biết vết thương, giữ lịch y tế sáng7/8 và222p. |
| 042 | 1927 → 1929 | 64 → 64 | Rowe qua ngưỡng trước thử vật và trở cùng đồ, không thử người lần nữa.; Cánh gỗ/then thường khác chốt đồng, khối thấp; thử gỗ/dây chưa chứng minh mọi vật hay mọi người; báo ngay. |
| 043 | 1889 → 1883 | 64 → 64 | Chỉ thoát nhờ xe/nhân chứng, không thắng tay đôi; tay phải đau tăng, tay áo trái được Nell kéo.; Giữ hai người/hai bao/đường ra phố và không biết tiếng giày sau lưng do vấp hay dừng; không vào cửa thấp. |
| 044 | 1904 → 1907 | 53 → 53 | Giữ scar trái cũ khác chấn thương phải, khám4p/ăn2p/còn215p; không tự khỏi.; Đội tới8/8 không là lệnh chờ khẩn; Marsh vẫn chưa tiếp xúc Jonah; không ghi người trẻ theo ra cổng là fact. |
| 045 | 1901 → 1901 | 61 → 61 | Mira chỉ môi giới có giá/không xác minh tổ chức; chưa trả12p tới046.; Ba phiếu thử không là công thức/khảo cứu riêng; chưa nhận Seq8 hay năng lực; tiếp nhận đội chiều8/8 giữ nguyên. |
| 046 | 1927 → 1929 | 51 → 51 | 12p là phí tra riêng, không quyền đọc/công thức; chỉ mục cần xin phép riêng.; Hai tên hãng chưa thành đổi tên tới thông báo thương mại; hai bộ phận và phụ trương giữ đủ. |
| 047 | 1851 → 1850 | 52 → 52 | Nguồn B là Silas tự kể, không nâng thành tận mắt; vật từ B qua chưa đủ khái quát.; Khối thấp/chốt đồng khác then gỗ, hai khung cố định cách12foot6inch; không tháo nền khi phòng người chỉ có lời Silas. |
| 048 | 1866 → 1864 | 48 → 48 | Thang tháo chưa rõ ai/ngày, lan can và dầm chưa phá; không đồng nhất hatch với đường cáng.; Đồ gửi vào chưa xác nhận tới giường, chưa có tiếng Jonah; phạm vi thợ/Nell và khung chịu lực được giữ. |
| 049 | 1914 → 1917 | 49 → 49 | Nêm chịu khoảng5giây không tạo đường mở; khối thấp/chốt chính đóng, chưa nâng từ ngoài.; Không đưa cáng hay người thử; phá sâu/bắn mù vẫn chưa bảo đảm bệnh nhân; gỗ mẫu được giữ riêng. |
| 050 | 2017 → 2023 | 39 → 39 | Thư7/8 không biết9/8; Dale có alibi khoảng đã đối, không vô can hoàn toàn; không giám định chữ tờ đã mất.; Mercer/Pike khác người, Jonas không nhớ thêm; hai vụ hành hung chưa nối, không nối Backlund; Mara không mất nợ/hai shilling tự về. |
| 051 | 1833 → 1836 | 75 → 75 | Giữ POV Mara, thư 9/8 chưa gửi; không truyền tin Backlund mới.; Giữ khoản nợ cũ/hai shilling và quyền tự quyết Theo; không đổi thoại.; “Để chiếc kéo sang bên” chỉ làm rõ danh từ dụng cụ may trong cảnh tháo chỉ; không đổi cảnh. |
| 052 | 1818 → 1822 | 71 → 71 | Không nhận diện Edith bằng POV Evan; giữ lời tự xưng/giọng Nell và việc chưa thấy mặt.; Không diễn giải tiếng động thành hành hung; giữ bác sĩ chưa khám và Jonah chưa trực tiếp nói. |
| 053 | 1850 → 1852 | 58 → 58 | Edith xin giúp cả hai không thay lời Jonah; vật liệu không thành chẩn đoán.; Giữ chốt/khay/cánh che và tiếp xúc y tế chưa thông đường; không đổi giờ hay tiền. |
| 054 | 1889 → 1886 | 61 → 61 | Không biến lối bò Edith thành lối cáng hay lối ra luôn mở; giữ điều kiện khóa và Silas đứng cạnh.; Giữ nguồn lần B là lời Edith, lần A là Evan thấy; Jonah chưa trực tiếp xin ra. |
| 055 | 1849 → 1853 | 54 → 54 | Jonah trực tiếp cho tên/đòi khám/ra, không thêm chẩn đoán hoặc cho chân chịu tải.; Bệ chỉ một người, không đầu cầu; giữ ô thoáng/không bước qua khoảng trống. |
| 056 | 1849 → 1858 | 53 → 53 | Khóa rào thường không thay chốt đồng; không đổi luật A/B.; Giữ giá đóng kho/nguồn Agnes ghi nghỉ việc và Silas chỉ thấy từng phần phương án. |
| 057 | 1852 → 1857 | 40 → 40 | Giữ sáu foot, cửa ở nhánh riêng và lỗ chỉ dụng cụ/đèn.; Nêm guide 40s/22s/25s khác nêm đồng 5s; chưa có dự phòng đạt trước khi thử. |
| 058 | 1858 → 1859 | 34 → 34 | Hai bộ thử độc lập, không cộng lực; dự phòng không được nâng thành bất hoại.; Không đổi thông số 6m40/22/25/40, quyền lựa chọn Edith hay Jonah còn trên giường. |
| 059 | 1857 → 1858 | 46 → 46 | Silas phá điểm giằng bằng dụng cụ, không tay không/phá dầm; không người trên cầu.; Dự phòng còn nhưng phần dẫn phải kiểm lại; không hứa cứu chắc sáng hôm sau. |
| 060 | 1807 → 1811 | 44 → 44 | Thử khôi phục bằng bộ dự phòng riêng, chưa mở lượt thật; nêm chưa nhận tải.; Giữ dây báo nhẹ không dây cáng, tay phải chưa hồi phục; không tự chứng kiến trang đêm. |

Đã đối chiếu 30/38 chương thuộc arc. Bản gốc nằm trong Git tại commit nguồn; không xóa hoặc viết đè lịch sử.
