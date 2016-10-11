## Vietnamese NLP

## Publications

<div class="papers" gid="147QdXmHU38Ru7tHYrANXUgvMWzek7Zxi8EkUo-m0unE"></div>
<div class="clear-fix"></div>

## Part I. Core Problems

### 1.1 Dictionaries

* [2004, Hồ Ngọc Đức, The Free Vietnamese Dictionary Project](http://www.informatik.uni-leipzig.de/~duc/Dict/)

### 1.2 Wordnet

* [viet wordnet](http://viet.wordnet.vn/wnms/editor/search/by-word/y%C3%AAu/2%7Cv)

### 1.3 Corpus

**<a href="http://viet.jnlp.org/download-du-lieu-tu-vung-corpus" target="_blank">VNESEcorpus</a>**, 650.000 sentences, 10.000 articles from vietnamnet.vn, dantri.com.vn, nhanhdan.com.vn. Size: 64.59 Mb

**<a href="http://viet.jnlp.org/download-du-lieu-tu-vung-corpus" target="_blank">VNTQcorpus(small)</a>**, 300.000 sentences, 1.000 articles from vnthuquan.net
Size: ~35 Mb

**<a href="http://viet.jnlp.org/download-du-lieu-tu-vung-corpus" target="_blank">VNTQcorpus(big)</a>**, 1.750.000 sentences, 13.000 articles from vnthuquan.net, Size: ~240 Mb

### 1.4 [Sentence Segmentation](http://magizbox.com/index.php/machine-learning/ds-applications/natural-language-processing/sentence-segmentation/)

Unknown

### 1.5 Word Segmentation

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **[Vitk](https://github.com/phuonglh/vn.vitk)** `spark`

Authors: [Le Hong Phuong](http://mim.hus.vnu.edu.vn/phuonglh)
Date: May 08, 2016

This is the first release of a Vietnamese text processing toolkit, which is called "Vitk", developed by Phuong LE-HONG at College of Natural Sciences, Vietnam National University, Hanoi.

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **[vnTokenizer](http://mim.hus.vnu.edu.vn/phuonglh/softwares/vnTokenizer)** `java`

Authors: [Le Hong Phuong](http://mim.hus.vnu.edu.vn/phuonglh)
Date: September 28, 2009

vnTokenizer is a software for tokenizing Vietnamese texts. It segments Vietnamese texts into lexical units (words, names, dates, numbers and other regular expressions) with a high accuracy, of about 98% on a test set extracted from the Vietnamese treebank.

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png)  **<a href="http://jvnsegmenter.sourceforge.net/" target="_blank">JVnSegmenter</a>** `java`

Authors: Cam-Tu Nguyen (ncamtu@gmail.com), Xuan-Hieu Phan (pxhieu@gmail.com)
Date: Mar 24, 2007

A Java-based Vietnamese Word Segmentation Tool

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **<a href="https://github.com/rockkhuya/DongDu" target="_blank">DongDu</a>** `C++`

Authors: rockkhuya(<a href="mailto:rockkhuya@gmail.com">rockkhuya@gmail.com</a>)

A Vietnamese word segmentation tool.

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **[Roy_VnTokenizer](https://github.com/roy-a/Roy_VnTokenizer)** `python`

Authors: Anindya Roy
Date: Jan 22, 2014

Vietnamese tokenization

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **<a href="http://vlsp.vietlp.org:8080/demo/?page=seg_pos_chunk" target="_blank">Online Tool from VLSP</a>** `online`

Not Available

### 1.6 Part-of-speech tagging (POS Tagging)

VCCorp 2016: 94.5% [^1]
Vitk 2016: accurary 95% (Vietnamese Tree Bank)

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **[Vitk](https://github.com/phuonglh/vn.vitk)** `spark`

Authors: [Le Hong Phuong](http://mim.hus.vnu.edu.vn/phuonglh)
Date: May 08, 2016

The part-of-speech tagger of Vitk can tag about 1,105,000 tokens per second, on a single machine, giving an accuracy of about 95% on the Vietnamese treebank.

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **<a href="http://mim.hus.vnu.edu.vn/phuonglh/softwares/vnTagger" target="_blank">vnTagger</a>** `java`

Vietnamese part-of-speech tagging

Authors: [Le Hong Phuong](http://mim.hus.vnu.edu.vn/phuonglh)
Date: Aug 05, 2010

**Paper**

* ![](http://icons.iconarchive.com/icons/graphicloads/folded/24/doc-page-folded-icon.png) [Le Hong Phuong, 2010, An empirical study of maximum entropy approach for part-of-speech tagging of Vietnamese texts](http://mim.hus.vnu.edu.vn/phuonglh/node/40)

### 1.7 Coreference

VCCorp 2016: 57% [^1]

**Thesis & Papers**:

* ![](http://icons.iconarchive.com/icons/graphicloads/folded/24/doc-page-folded-icon.png) [2011, Giải quyết bài toán đồng tham chiếu trong văn bản tiếng việt dựa vào phương pháp máy vector hỗ trợ SVM](http://www.coltech.vnu.edu.vn/~thuyhq/Student_Thesis/K52_Le_Duc_Trong_Thesis.pdf)

### 1.8 Dependency Grammar

VCCorp 2016: 73% [^1]

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/doc-page-folded-icon.png) [2013, Nguyễn Vi Dương, Nguyễn Thị Đảm, Bộ chuyển đổi từ văn phạm thành phần sang văn phạm phụ thuộc cho tiếng Việt](https://bitbucket.org/epilab/vnlp/downloads/DependencyGrammarForVNese.doc)

### 1.9 Chunking

VCCorp 2016: 83% [^1]

### [1.10 Named Entity Recognition (NER)](http://magizbox.com/index.php/machine-learning/ds-applications/natural-language-processing/name-entity-recognization/)

VCCorp 2016: 84.8% [^1]

**Papers**:

* ![](http://icons.iconarchive.com/icons/graphicloads/folded/24/doc-page-folded-icon.png) [2007, Named Entity Recognition in Vietnamese documents](https://www.nii.ac.jp/pi/n4/4_5.pdf)
* ![](http://icons.iconarchive.com/icons/graphicloads/folded/24/doc-page-folded-icon.png) [2005, Named Entity Recognition in Vietnamese Free-Text and Web Documents Using Conditional Random Fields](http://lamda.nju.edu.cn/nguyenct/files/papers/ncamtu-09-paper_ner.pdf)

### 1.11 Relations Extraction Systems

Unknown

### 1.12 Sentiment Analysis

![](http://icons.iconarchive.com/icons/graphicloads/folded/24/setting-folded-icon.png) **[Sentiment Analysis](https://bitbucket.org/epilab/vnlp/downloads/sentiment-analysis.zip)** `java`

Authors: [Epi Lab](https://bitbucket.org/epilab/)
Date: Aug 01, 2013

### 1.13 Language Identification

Unknown

## Part 2. Vietnamse NLP Groups

**Groups**

* [vnlp.net, (2010-now)](http://vnlp.net/)
* [kde lab, (2014-now)](http://kde.soict.hust.edu.vn/)

**People**

* [Assoc. Prof. Ha Quang Thuy](http://www.coltech.vnu.edu.vn/~thuyhq/)
* [Prof. Tu-Bao Ho](http://www.jaist.ac.jp/~bao/)
* [Khoat Than](http://is.hust.edu.vn/~khoattq/)
* [Cam Tu Nguyen](http://www.dais.is.tohoku.ac.jp/~ncamtu/index.htm)
* [CAM-TU NGUYEN](http://lamda.nju.edu.cn/nguyenct/?AspxAutoDetectCookieSupport=1)
* [Le Hong Phuong](http://mim.hus.vnu.edu.vn/phuonglh/)
* [Phan Xuan Hieu](https://sites.google.com/site/pxhieu/)
* [Trần Mai Vũ](http://fit.uet.vnu.edu.vn/gioi-thieu/giang-vien/vutm/)
* [Nguyễn Kiêm Hiếu](http://soict.hust.edu.vn/index.php/bo-mon-trung-tam/he-thong-thong-tin/can-bo/227-ts-nguyen-kiem-hieu)

## Part 3. Applications

### [VAV - Trợ lý ảo cho người Việt](https://play.google.com/store/apps/details?id=com.mdnteam.vav)

Date: Nov 2015 - now

<img src="https://lh3.googleusercontent.com/TOdXdeSwJ6qQy4gYqWJbPbep8Sb82h9oZPsor3WWXyi72HafO3xttiBlD-dpnKAahyY=h900-rw" style="height:80px"/>

**MDN-Team, Khoa CNTT, Trường ĐH Công nghệ, ĐHQG HN Tools**

> Bạn đang nghĩ đến một ứng dụng thông minh trên di động cho phép bạn tương tác bằng giọng nói để hẹn chuông báo thức, đặt lịch cho một cuộc họp, bật định vị, gọi điện cho ai đó, truy cập một trang web bất kỳ, tìm đường trên bản đồ, định vị cây ATM của một ngân hàng nào đó gần với bạn, hay thưởng thức một bản nhạc mình yêu thích … Ứng dụng Trợ lý ảo VAV chính là câu trả lời cho bạn.
> Được thiết kế và phát triển dựa trên các kỹ thuật trí tuệ nhân tạo (học máy, phân tích và hiểu ngôn ngữ tự nhiên), VAV có thể hiểu được ý định của bạn dù bạn diễn đạt câu lệnh của mình theo nhiều cách khác nhau mà không cần tuân theo bất kỳ khuôn mẫu nào cho trước. Những gì VAV hướng tới là trở thành một trợ lý ảo thông minh giúp bạn thực hiện những điều mình muốn và là một người đồng hành thân thiện, dí dỏm bên bạn.

[^1]: [2016, Big Challenges for Data Scientists at VCCORP](https://drive.google.com/file/d/0B6LYda0EhWbSelc2VTlZVFZia1E/view?usp=sharing)

