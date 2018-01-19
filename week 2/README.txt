*** VISUALIZE MÔ HÌNH SVM KHI THAY ĐỔI THAM SỐ ***
Từ khi ra đời vào năm 2014, Jupyter Notebook nhanh chóng trở thành công cụ giúp các nhà khoa học tương tác hiệu quả trong Khoa học dữ liệu và Tính toán khoa học với tất cả các ngôn ngữ lập trình.
Jupyter cho phép các nhà phân tích dữ liệu xử lý và kiểm tra các mô hình với mọi ngôn ngữ (Python, C++, R, Julia, Ruby, Lua, Haskell, và nhiều hơn thế nữa). Với giao diện đơn giản, Jupyter vẫn cho phép người dùng render dữ liệu, văn bản và đồ họa phức tạp, làm cho một dự án khoa học dữ liệu / máy học tập trở nên sống động trong tất cả đỉnh cao của nó.

Tuy nhiên, quá trình học và thử nghiệm với dữ liệu bị đắm chìm trong việc tương tác với các tham số của mô hình và xem ảnh hưởng của các tham số đó lên mô hình trong thời gian thực. Hầu hết các render hiện tại của Jupyter đều là tĩnh.
Để giải quyết vấn đề này, chúng ta sẽ sử dụng một widget mới của Jupyter là "ipywidgets". Widget này cho phép chúng ta tương tác và render trực tiếp mô hình cũng như hiển thị đồ họa của mô hình trong thời gian thực, thông qua việc tùy chỉnh các tham số của mô hình.

** CÀI ĐẶT **
Có 2 cách để cài đặt "ipywidgets" trong Jupyter.
* Sử dụng PIP
Sử dụng dòng lệnh sau để cài và cho phép "ipywidgets" chạy trong Jupyter
$ pip install ipywidgets
$ jupyter nbextension enable --py widgetsnbextension

* Sử dụng CONDA
Trong trường hợp bạn sử dụng Anaconda, "ipywidgets" sẽ được bật một cách tự động.
$ conda install -c conda-forge ipywidgets

Để tìm hiểu thêm về "ipywidgets", xem chi tiết tại đây: https://ipywidgets.readthedocs.io/