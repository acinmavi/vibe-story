# Báo cáo biên tập văn phong Arc 1 — 001–030

Ngày 04/11/2026. Nhánh `edit/prose-polish-arc1`. Nguồn so sánh: commit `8e838312e8c5560d00e637a4feaf08613f67989c`.

Người dùng duyệt bản thử003 và STYLE_GUIDE, cho phép sửa toàn bộ Arc1 gồm001 đã khóa, rồi yêu cầu tiếp Arc2. Không viết thêm chương, không push/merge; không đổi trạng thái duyệt arc.

## Phương pháp và phạm vi QA

Đọc trọn từng chương và phần nối, chọn chuỗi câu rời có cùng trọng tâm. Giữ lời thoại, khoảng ngắt nghệ thuật, điểm nhìn, mức chắc chắn, nguồn và vị trí vật chứng. Đề xuất được soát semantic trước khi áp dụng; loại mọi chỗ có thể thêm tác nhân, mục đích, vị trí hoặc độ chắc chắn. Không thêm cảnh hoặc làm dài để đạt chỉ tiêu từ.

Số từ đếm bằng split(), gồm tiêu đề; đoạn là khối cách bởi dòng trắng, không tính tiêu đề. Mỗi chương có kiểm máy riêng: tiêu đề, nguyên chuỗi chữ số, nguyên toàn bộ trích dẫn kép/đơn theo thứ tự, biến động độ dài. Script dự án kiểm cấu trúc và cổng duyệt; máy không tự chứng minh tương đương ngữ nghĩa hoặc chất lượng văn.

## Đối chiếu từng chương

| Chương | Từ trước → sau | Đoạn trước → sau | Trọng điểm bảo toàn |
|---|---:|---:|---|
| 001 | 3000 → 3000 | 139 → 139 | Giữ các nhịp đứt của cú sốc xuyên không, tin nhắn, tên tự hiện và tiếng gọi; nối miêu tả cùng chủ thể, không lý giải dị tượng. |
| 002 | 2159 → 2175 | 121 → 121 | Giữ đếm Một. Hai. Ba., việc chỉ ký nhận hòm, mất tiền kiểm và nhịp gãy chì; nối việc đọc phiếu, học thao tác và đường về phòng. Hai câu ngắn được kiểm và giữ nguyên. |
| 003 | 2162 → 2210 | 128 → 128 | Áp dụng bản thử003 đã duyệt, hoàn nguyên suy diễn vị trí đứng bên bàn sau review độc lập; giữ C2, thiếu hiểu biết nghề giấy và các câu ngắn. |
| 004 | 2241 → 2254 | 111 → 111 | Giữ thứ tự mua đúng mẫu, lịch, bỏ bản đồ, bữa ăn và nghe Tingen/Loen; không tăng khả năng nhận diện hoặc đổi tiền. |
| 005 | 2194 → 2201 | 93 → 93 | Giữ thông báo chỉ tìm thông tin, không thành cáo phó; giữ ký ức sách riêng với chứng cứ. Giữ nhịp tên Welch/Naya, Chỉ bấy nhiêu và Không mắc. |
| 006 | 2066 → 2071 | 121 → 121 | Giữ mọi giới hạn nhân chứng: Mara đến sau dỡ hòm; Jonas không chắc ngày, mặt, tên và cuối chuyến. Không biến cầm phiếu thành ký nhận; giữ mất lượt công và cuối chương không buông giấy. |
| 007 | 2317 → 2320 | 97 → 97 | Giữ ngày 3/7, tiền ăn ghi nợ và năm penny; giữ sự bất định về lịch Klein, tháng chín và ngưỡng cầu cứu ngay nếu có nạn nhân. Không chọn con đường sớm. |
| 008 | 1994 → 1992 | 126 → 126 | Giữ 12sh lương cũ, đổi 1sh để trả 6p, trả Ada 3sh+3p, còn104p; không quy Kestrel thành chủ mưu. Giữ quyền quyết định của Mara và giới hạn lời hứa giúp Theo. |
| 009 | 2051 → 2040 | 118 → 118 | Giữ317 trên gỗ/371 trên phiếu, chưa chắc cùng kiện; Bram chỉ xác nhận việc xem hai số, không xác nhận nguồn gốc/thứ tự. Giữ phí1p, còn103p, không lấy hòm/phiếu gốc. |
| 010 | 2312 → 2313 | 107 → 107 | Giữ kho xe/kho sau, khoảng rời mắt và khả năng đổi tờ; không chứng minh dấu sửa ký ức. Giữ bỏ lượt xem sổ để bảo vệ nguồn, tìm hiệu sách có điều kiện, không đặt cọc. |
| 011 | 2001 → 2007 | 113 → 113 | Phí 1 shilling, 103→91 penny; nguồn công thức chưa khớp, Iona chỉ là lời giới thiệu. Giữ thoại/câu ngắn nhấn; nối các chuỗi quan sát và thao tác cùng trọng tâm. |
| 012 | 2059 → 2060 | 89 → 89 | Giữ nguyên 317, kho sau, giới hạn không xác nhận cùng tờ; rãnh ép không thành chữ, không thành năng lực. Giữ thoại/câu ngắn nhấn; nối các chuỗi quan sát và thao tác cùng trọng tâm. |
| 013 | 2221 → 2225 | 97 → 97 | 12 pound còn ký thác; kiểm sai được sửa, quyền mua chưa thành giao dịch. Giữ thoại/câu ngắn nhấn; nối các chuỗi quan sát và thao tác cùng trọng tâm. |
| 014 | 2061 → 2073 | 101 → 101 | Bản chép Bram bị lấy, gốc và bản vẽ vẫn ở nơi cũ; thủ phạm chưa xác định. Giữ thoại/câu ngắn nhấn; nối các chuỗi quan sát và thao tác cùng trọng tâm. |
| 015 | 1998 → 1989 | 127 → 127 | Mara nói dối vị trí Theo nhưng chưa dùng tên Evan; lòng tin chưa khôi phục. Giữ thoại/câu ngắn nhấn; nối các chuỗi quan sát và thao tác cùng trọng tâm. |
| 016 | 2172 → 2163 | 116 → 116 | Gideon chỉ nhận đổi mục/đóng dấu; chưa giải cơ chế; chìa khóa chỉ mở khi ông có mặt.; Giữ nguyên thoại, dữ kiện, thứ tự và mức chắc chắn; câu ngắn ở phát hiện được giữ. |
| 017 | 2102 → 2099 | 80 → 80 | 150−12=138 pound; chưa nhận nguyên liệu; bản tường trình 15/7 vẫn được nộp riêng.; Giữ nguyên thoại, dữ kiện, thứ tự và mức chắc chắn; câu ngắn ở phát hiện được giữ. |
| 018 | 2097 → 2107 | 78 → 78 | Nợ132 pound, hạn2 pound/tháng từ31/8; đồng hồ bán6 pound; chưa uống trước20/7.; Giữ nguyên thoại, dữ kiện, thứ tự và mức chắc chắn; câu ngắn ở phát hiện được giữ. |
| 019 | 2294 → 2297 | 97 → 97 | Seq9 chưa thành thạo; vệt xám không điều khiển được, đau/tiếng nói/đứt nhớ giữ nguyên.; Giữ nguyên thoại, dữ kiện, thứ tự và mức chắc chắn; câu ngắn ở phát hiện được giữ. |
| 020 | 2007 → 2017 | 93 → 93 | Không đưa người mới tiếp xúc; mẫu ít và giới hạn khác nhau; linh thị không cho thấy liên kết.; Giữ nguyên thoại, dữ kiện, thứ tự và mức chắc chắn; câu ngắn ở phát hiện được giữ. |
| 021 | 2037 → 2034 | 86 → 86 | Tiếng nói suýt buộc nhầm Bram; bản vẽ chỉ bác việc đủ nét đối, không chứng minh vô can.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 022 | 2139 → 2135 | 101 → 101 | Theo tự chọn trả đồ; mất cơ hội theo tuyến; cuộc gặp24/7 giữ nguyên, phiếu371 không biến thành trang sổ.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 023 | 2098 → 2095 | 102 → 102 | Kestrel chỉ đề nghị mua nợ; chưa xóa nợ, biết chỗ sửa có thể qua Gideon; lịch chỉ là bản chép chưa xác nhận.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 024 | 1925 → 1925 | 79 → 79 | Nguồn tác động chưa đủ xác định toàn bộ; ngày kiểm28/7 không thành cứu viện đã tới; bản vẽ tách riêng.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 025 | 2243 → 2248 | 96 → 96 | Không xác nhận xe/thủ phạm; 2sh Mara mất riêng, 76penny Evan giữ; gốc ngoài hệ chưa mất.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 026 | 2038 → 2041 | 72 → 72 | Kestrel ở cột người thuê; phiếu371 và sổ là hai nguồn; rãnh ép không tự viết tên hoặc đầy đủ mã.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 027 | 2092 → 2096 | 75 → 75 | Gideon tự mở ngăn; nhân sự chuyên trách quản thúc Phiếu17, Evan không sở hữu; trách nhiệm và mất công vẫn đủ.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 028 | 2137 → 2138 | 86 → 86 | Chưa ghi sai khác mới không thành hết mọi nguy cơ; nợ132, 12 đã khấu trừ; Mara còn khoảng cách.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 029 | 2035 → 2039 | 78 → 78 | Nợ132; trả48penny còn28; chưa hoàn thiện tiêu hóa; việc nghiên cứu thường không chứng minh biết nghề.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |
| 030 | 2004 → 2010 | 73 → 73 | 27penny; Backlund chưa nhận việc/ứng tiền/vé; quyền3bản và nợ132 tiếp diễn; nguồn xám chưa xác định.; Không sửa thoại, dấu chứng cứ; giữ thứ tự, tri thức hạn chế, rủi ro và quyền quyết định nhân vật. |

Đã đối chiếu 30/30 chương thuộc arc. Bản gốc nằm trong Git tại commit nguồn; không xóa hoặc viết đè lịch sử.
