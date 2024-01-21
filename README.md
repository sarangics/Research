# Research
Data set selection
The data set Ham and Spam emails from spam Assassin provide at ](https://www.kaggle.com/veleon/ham-and-spam-dataset). It contains several spam and non-spam email files all readable by Python Email Library.

1.Import libraries.

2.Get the directory segmentation.
	['ham', 'hamnspam', 'spam']
 
3.Reading Data Set Files Records and dataset structure.
	Amount of ham emails:  2551
	Amount of spam emails:  501
	Spam percentage:  16.41546526867628 %
 
4.Load an email and check how it looks like. (Using email.parser-https://docs.python.org/3/library/email.parser.html)



	Header field names:  ['Return-Path', 'Delivered-To', 'Received', 'Received', 'Received', 'Received', 'Delivered-To', 'Received', 'Received', 'Received', 'Received', 'Received', 'Received', 'From', 'To', 'Cc', 'Subject', 'In-Reply-To', 'References', 'MIME-Version', 'Content-Type', 'Message-Id', 'X-Loop', 'Sender', 'Errors-To', 'X-Beenthere', 'X-Mailman-Version', 'Precedence', 'List-Help', 'List-Post', 'List-Subscribe', 'List-Id', 'List-Unsubscribe', 'List-Archive', 'Date']

 -------------------------------------- 

Message field values:  ['<exmh-workers-admin@example.com>', 'zzzz@localhost.netnoteinc.com', 'from localhost (localhost [127.0.0.1])\tby phobos.labs.netnoteinc.com (Postfix) with ESMTP id D03E543C36\tfor <zzzz@localhost>; Thu, 22 Aug 2002 07:36:16 -0400 (EDT)', 'from phobos [127.0.0.1]\tby localhost with IMAP (fetchmail-5.9.0)\tfor zzzz@localhost (single-drop); Thu, 22 Aug 2002 12:36:16 +0100 (IST)', 'from listman.example.com (listman.example.com [66.187.233.211]) by    dogma.slashnull.org (8.11.6/8.11.6) with ESMTP id g7MBYrZ04811 for    <zzzz-exmh@example.com>; Thu, 22 Aug 2002 12:34:53 +0100', 'from listman.example.com (localhost.localdomain [127.0.0.1]) by    listman.redhat.com (Postfix) with ESMTP id 8386540858; Thu, 22 Aug 2002    07:35:02 -0400 (EDT)', 'exmh-workers@listman.example.com', 'from int-mx1.corp.example.com (int-mx1.corp.example.com    [172.16.52.254]) by listman.redhat.com (Postfix) with ESMTP id 10CF8406D7    for <exmh-workers@listman.redhat.com>; Thu, 22 Aug 2002 07:34:10 -0400    (EDT)', '(from mail@localhost) by int-mx1.corp.example.com (8.11.6/8.11.6)    id g7MBY7g11259 for exmh-workers@listman.redhat.com; Thu, 22 Aug 2002    07:34:07 -0400', 'from mx1.example.com (mx1.example.com [172.16.48.31]) by    int-mx1.corp.redhat.com (8.11.6/8.11.6) with SMTP id g7MBY7Y11255 for    <exmh-workers@redhat.com>; Thu, 22 Aug 2002 07:34:07 -0400', 'from ratree.psu.ac.th ([202.28.97.6]) by mx1.example.com    (8.11.6/8.11.6) with SMTP id g7MBIhl25223 for <exmh-workers@redhat.com>;    Thu, 22 Aug 2002 07:18:55 -0400', 'from delta.cs.mu.OZ.AU (delta.coe.psu.ac.th [172.30.0.98]) by    

 -------------------------------------- 
 

Message content:     Date: 


Data Preprocessing.
Feature Extraction


5. Extract some of main email fields. (sender, receiver and subject)
   
	Email from:  ['Robert Elz <kre@munnari.OZ.AU>']
	Email to:  ['Chris Garrigues <cwg-dated-1030377287.06fa6d@DeepEddy.Com>']
	Email subject:  ['Re: New Sequences Window']
 

6.Import all emails.
	
	['Re: New Sequences Window']
    Date:        Wed, 21 Aug 2002 10:54:46 -0500
    From:        Chris Garrigues <cwg-dated-1030377287.06fa6d@DeepEddy.Com>
    Message-ID:  <1029945287.4797.TMDA@deepeddy.vircio.com>


  | I can't reproduce this error.

For me it is very repeatable... (like every time, without fail).



Converting emails to plain text

	 
7.Check email content types

	Ham content types:  {'multipart/report', 'text/plain', 'multipart/alternative', 'multipart/mixed', 'multipart/related', 'multipart/signed'}
	Spam content types:  {'text/plain', 'multipart/alternative', 'multipart/mixed', 'multipart/related', 'text/html'}

8.Check multipart email content types/structure


	Ham content types:  {'multipart(multipart(text/plain, text/plain, text/plain), application/pgp-signature)', 'multipart(text/plain, video/mng)', 'text/plain', 'multipart(text/plain, text/enriched)', 'multipart(text/plain, application/ms-tnef, text/plain)', 'multipart(text/plain, text/plain)', 'multipart(text/plain, application/x-pkcs7-signature)', 'multipart(text/plain, multipart(text/plain, text/plain), text/rfc822-headers)', 'multipart(text/plain, application/x-java-applet)', 'multipart(text/plain, application/pgp-signature)', 'multipart(text/plain)', 'multipart(text/plain, application/octet-stream)', 'multipart(text/plain, multipart(text/plain, text/plain), multipart(multipart(text/plain, application/x-pkcs7-signature)))', 'multipart(text/plain, text/html)', 'multipart(text/plain, multipart(text/plain))'}
Spam content types:  {'multipart(multipart(text/plain, text/html), image/gif)', 'multipart(multipart(text/html), application/octet-stream, image/jpeg)', 'text/plain', 'multipart(text/html, application/octet-stream)', 'multipart/alternative', 'multipart(multipart(text/html))', 'multipart(text/plain)', 'multipart(text/html, text/plain)', 'multipart(text/plain, image/jpeg)', 'multipart(text/plain, application/octet-stream)', 'multipart(text/html)', 'text/html', 'multipart(text/plain, text/html)'}

9.Convert HTML emails to plain format.
	 
10.Convert all HTML emails to plain text.

	Save up to 70% on Life Insurance. Why Spend More Than You Have To?Life Quote Savings Ensuring your family's financial security is very important. Life Quote Savings makes buying life insurance simple and affordable. We Provide FREE Access to The        Very Best Companies and The Lowest Rates.Life Quote Savings is FAST, EASY, and              SAVES you money! Let us help you get started with the best values in the country on new coverage. You can SAVE hundreds or even thousands of dollars by requesting a FREE quote from Lifequote Savings. Our              service will take you less than 5 minutes to complete. Shop and compare. SAVE up to 70% on all types of Life insurance! Click Here For Your              Free Quote!Protecting your family is the best investment you'll ever            make! If you are in receipt of this email in error and/or wish to be removed from our list, PLEASE CLICK HERE AND TYPE REMOVE. If you reside in any state which prohibits e-mail solicitations for insurance,        please disregard this email. 



Dear Partner to be,

First, I must apologise to you for using this medium to communicate to you
about this project.

I am a highly placed official of  Government of Nigeria and also a
founding member of the ruling party in Power now,the Peoples Democratic
Party(PDP).

My committee - The Niger Delta Development Corporation(NDDC)-which is in
charge of managing and supervising  the disbursement of oil sales revenues
for the Nigerian government.The revenues  under our control runs into
several hundred of millions of dollars monthly.My self and   
other colleagues in the NDDC are currently in need of a foreign partner
with whose bank account we shall transfer the sum of Forty Nine Million
Five Hundred Thosand United States Dollars($49.5m).This fund accrued to us
as commission for oil sales contracts handled under our supervision.

The fund is presently waiting in the Government Account named CBN/FGN
INDEPENDENT REVENUE account number 400-939134 with J.P.MORGAN CHASE
BANK,New York.You can do




11.Removing unknown encoding with spam emails.

Building the dataset to train a data model

12. Create a data frame with the email’s content and their particular label. (ham-0,spam-1)
	 
	
13.Shuffle the data set

	 
	
	
	
14.Removing special characters from the data frame. And convert to lowercase letters

	Email content	Label
0	hello fork so they have aaron schwartz on n...	0
1	on mon 2 sep 2002 reza b'far ebuilt wrote: w...	0
2	url: http://www.askbjoernhansen.com/archives/2...	0
3	snip misc rants about finding jobs java vs c w...	0
4	url: http://diveintomark.org/archives/2002/09/...	0
In [28]:

	
15.Preprocess the input.

16.Split to the training and testing sets.

	X_train:  2440
	X_test:  610
	Y_train:  2440
	Y_test:  610


Using MultiNomial Naive Bayes as the Model with CountVectorizer
	
Precision: 97.27%
Accuracy: 98.03%
Recall: 92.24%
F1 score: 94.69%


array([[491,   3],
       [  9, 107]], dtype=int64)






SVC with Countvectorizer
Precision: 98.10%
Accuracy: 99.02%
Recall: 96.26%
F1 score: 97.17%


array([[501,   2],
       [  4, 103]], dtype=int64)




Data Set Cleaning

1.Without any Changing.
	Data Frame
 ![image](https://github.com/sarangics/Research/assets/65746767/8a671b87-e8cc-4345-bbfe-654b4988251d)

Using MultiNomial Naive Bayes as the Model with CountVectorizer
![image](https://github.com/sarangics/Research/assets/65746767/a9f4900a-50f6-4102-867f-6244e2dc7982)
SVC with Countvectorizer
![image](https://github.com/sarangics/Research/assets/65746767/92225c60-958e-4d51-96d0-02a79fddb4ab)
2.Removing special Characters and convert to lower cases.

![image](https://github.com/sarangics/Research/assets/65746767/6fa98ea4-8551-4ee2-b8b2-d0507f975903)
Using MultiNomial Naive Bayes as the Model with CountVectorizer
![image](https://github.com/sarangics/Research/assets/65746767/b6c494e2-aeba-481e-b8a1-a598db13e2c5)
SVC with Countvectorizer
![image](https://github.com/sarangics/Research/assets/65746767/ef75e92b-95b2-4301-97b6-97bee7886942)
3. Removing special Characters, email addresses, numbers, dates, whitespaces, URL’s and convert to lower case letters.
	Data Frame
![image](https://github.com/sarangics/Research/assets/65746767/58ca312d-41fd-4be3-b1fd-9fa0f5145d61)
Using MultiNomial Naive Bayes as the Model with CountVectorizer
![image](https://github.com/sarangics/Research/assets/65746767/3d32a7af-0ac0-4344-a6c5-73d12a5f0b0b)

SVC with Countvectorizer
![image](https://github.com/sarangics/Research/assets/65746767/b320fa8f-d5b5-49d4-94a3-c1942462f4fc)
4.Removing To:,From:,and Date: fields of emails with above changes.
Data Frame
![image](https://github.com/sarangics/Research/assets/65746767/a0f84846-a30b-43eb-a1de-eae63fcc5a51)
Using MultiNomial Naive Bayes as the Model with CountVectorizer
![image](https://github.com/sarangics/Research/assets/65746767/e5a169f4-4ec0-45dc-b07d-14706c9cce6d)
SVC with Countvectorizer
![image](https://github.com/sarangics/Research/assets/65746767/cacbb77e-76e8-4569-8aa2-1baf62fea954)
![image](https://github.com/sarangics/Research/assets/65746767/128c33f2-d9d9-43c5-bcb2-f18f9e655318)
Apply 5-fold cross validation method to the  spam assassin data set.
Apply 5-fold cross validation method to the  spam assassin data set.

(a). Without any changing.
	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.99180328 0.9897541  0.98770492 0.98360656 0.98155738]
[0.97468354 0.98701299 0.98684211 0.97368421 0.96103896]
[0.97468354 0.95       0.9375     0.925      0.925     ]
[0.97468354 0.96815287 0.96153846 0.94871795 0.94267516]
0.9868852459016395
0.9766523616290439
0.9424367088607595
0.9591535960075829
Precision: 97.67%
Accuracy: 98.69%
Recall: 94.24%
F1 score: 95.92%

	2. SVC with Countvectorizer
[0.97745902 0.98565574 0.98155738 0.98155738 0.99385246]
[0.98591549 0.92857143 0.94936709 0.97333333 0.98765432]
[0.875      0.975      0.9375     0.9125     0.98765432]
[0.92715232 0.95121951 0.94339623 0.94193548 0.98159509]
0.9840163934426229
0.9649683328915515
0.9375308641975308
0.9490597264773039
Precision: 96.50%
Accuracy: 98.40%
Recall: 93.75%
F1 score: 94.91%

(b). Removing special Characters and convert to lower cases.
	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.98155738 0.98565574 0.98360656 0.98360656 0.99180328]
[0.97297297 0.97402597 1.         0.98648649 0.975     ]
[0.91139241 0.9375     0.9        0.9125     0.975     ]
[0.94117647 0.95541401 0.94736842 0.94805195 0.975     ]
0.9852459016393442
0.9816970866970867
0.9272784810126582
0.9534021704863337
Precision: 98.17%
Accuracy: 98.52%
Recall: 92.73%
F1 score: 95.34%

	2. SVC with Countvectorizer
[0.97131148 0.96106557 0.98360656 0.99180328 0.9795082 ]
[0.91025641 0.94117647 0.97333333 0.96296296 0.93670886]
[0.92307692 0.81012658 0.92405063 0.98734177 0.93670886]
[0.91025641 0.8707483  0.94805195 0.975      0.93670886]
0.9774590163934427
0.9448876075800869
0.9162609542356378
0.928153103677516
Precision: 94.49%
Accuracy: 97.75%
Recall: 91.63%
F1 score: 92.82%

(c). Removing Special Characters, email addresses, numbers, dates, whitespaces, URL’s and convert to lower case letters.


	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.9897541  0.99385246 0.98360656 0.97540984 0.98770492]
[1.         0.98734177 0.98648649 0.925      1.        ]
[0.93670886 0.975      0.9125     0.925      0.925     ]
[0.96732026 0.98113208 0.94805195 0.925      0.96103896]
0.9860655737704918
0.979765651727677
0.9348417721518987
0.9565086492001031
Precision: 97.98%
Accuracy: 98.61%
Recall: 93.48%
F1 score: 95.65%

	2. SVC with Countvectorizer
[0.98360656 0.98155738 0.97540984 0.96106557 0.97540984]
[1.         0.91566265 0.92307692 0.87341772 0.93506494]
[0.8974359  0.97435897 0.92307692 0.88461538 0.91139241]
[0.94594595 0.94409938 0.92307692 0.87898089 0.92307692]
0.9754098360655739
0.9294444460526512
0.918175916910094
0.9230360125403051
Precision: 92.94%
Accuracy: 97.54%
Recall: 91.82%
F1 score: 92.30%



(d). (c)+Removing To:,From:,and Date: fields of emails with above changes.
(email fields)
.


	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.9897541  0.99385246 0.99180328 0.97540984 0.98565574]
[0.9625     1.         0.975      0.97222222 0.95061728]
[0.97468354 0.9625     0.975      0.875      0.9625    ]
[0.96855346 0.98089172 0.975      0.92105263 0.95652174]
0.987295081967213
0.9720679012345679
0.9499367088607595
0.9604039099148205
Precision: 97.21%
Accuracy: 98.73%
Recall: 94.99%
F1 score: 96.04%

	2. SVC with Countvectorizer
[0.98155738 0.97745902 0.97745902 0.97336066 0.98360656]
[0.92771084 0.96       0.93670886 0.925      0.98666667]
[0.9625     0.9        0.925      0.91358025 0.91358025]
[0.94478528 0.92903226 0.93081761 0.91925466 0.94871795]
0.978688524590164
0.9472172741599308
0.922932098765432
0.9345215502608142
Precision: 94.72%
Accuracy: 97.87%
Recall: 92.29%
F1 score: 93.45%


(e). (d)+Removing stop words, stemming and lemmatization the data set.
	

	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.97540984 0.95696721 0.94672131 0.96721311 0.95696721]
[0.93506494 0.8172043  0.80681818 0.86363636 0.83908046]
[0.91139241 0.95       0.8875     0.95       0.9125    ]
[0.92307692 0.87861272 0.8452381  0.9047619  0.8742515 ]
0.960655737704918
0.8523608482729728
0.9222784810126582
0.8851882273691833
Precision: 85.24%
Accuracy: 96.07%
Recall: 92.23%
F1 score: 88.52%

	2. SVC with Countvectorizer

[0.98360656 0.9692623  0.9692623  0.9897541  0.98770492]
[0.95945946 0.91891892 0.8875     0.96202532 0.97368421]
[0.92207792 0.88311688 0.92207792 0.97435897 0.94871795]
[0.94666667 0.90066225 0.9044586  0.96815287 0.96103896]
0.9799180327868852
0.9403175810720781
0.9300699300699302
0.936195868865882
Precision: 94.03%
Accuracy: 97.99%
Recall: 93.01%
F1 score: 93.62%


Before applying 5-fold cross validation
![image](https://github.com/sarangics/Research/assets/65746767/814547e2-988b-46cc-b472-445cb168542a)
After Applying 5-fold cross validation
![image](https://github.com/sarangics/Research/assets/65746767/4469fe34-ddec-4565-a44e-a6428b40ed82)
![image](https://github.com/sarangics/Research/assets/65746767/3920a7af-08ca-4a3d-b0c3-908e3614728e)
Apply 5-fold cross validation method to the Enron spam data set.

(a). Without any changing.
	1. Using Multinomial NaiveBayes as the Model with CountVectorizer 
[0.95578231 0.94444444 0.94217687 0.95351474 0.94892168]
[0.98550725 0.98477157 0.9947644  0.99502488 0.98994975]
[0.85       0.80833333 0.79166667 0.83333333 0.82083333]
[0.91275168 0.88787185 0.88167053 0.90702948 0.89749431]
0.9489680094512266
0.9900035684504482
0.8208333333333332
0.8973635697478362
Precision: 99.00%
Accuracy: 94.90%
Recall: 82.08%
F1 score: 89.74%

	2. SVC with Countvectorizer
[0.95124717 0.96825397 0.96938776 0.93764172 0.96367764]
[0.96788991 0.97402597 0.96610169 0.94444444 0.96521739]
[0.85425101 0.91093117 0.92307692 0.82591093 0.90243902]
[0.90752688 0.94142259 0.94409938 0.8812095  0.93277311]
0.9580416502582871
0.9635358825893803
0.8833218129752147
0.9214062934456232
Precision: 96.35%
Accuracy: 95.80%
Recall: 88.33%
F1 score: 92.14%

(b). Removing special Characters and convert to lower cases.
	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.93877551 0.95124717 0.94444444 0.94444444 0.95346198]
[0.98947368 0.99004975 0.99481865 0.98974359 0.98536585]
[0.78333333 0.82916667 0.8        0.80416667 0.84166667]
[0.8744186  0.90249433 0.88683603 0.88735632 0.90786517]
0.9464747079308455
0.989890306341235
0.8116666666666668
0.891794090761791
Precision: 98.99%
Accuracy: 94.65%
Recall: 81.17%
F1 score: 89.18%

	2. SVC with Countvectorizer
[0.96371882 0.95464853 0.95918367 0.96598639 0.95913734]
[0.95238095 0.95890411 0.97674419 0.94537815 0.97235023]
[0.91286307 0.87136929 0.87136929 0.92975207 0.87551867]
[0.93220339 0.91304348 0.92105263 0.9375     0.92139738]
0.9605349517786683
0.9611515259383511
0.8921744796131819
0.9250393759165977
Precision: 96.12%
Accuracy: 96.05%
Recall: 89.22%
F1 score: 92.50%

(c). Removing Special Characters, email addresses, numbers, dates, whitespaces, URL’s and convert to lower case letters.


	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.94331066 0.95578231 0.94104308 0.9478458  0.95800227]
[0.98969072 0.98550725 0.97959184 0.98989899 0.99512195]
[0.8        0.85       0.8        0.81666667 0.85      ]
[0.88479263 0.91275168 0.88073394 0.89497717 0.91685393]
0.949196825911598
0.9879621491758985
0.8233333333333333
0.8980218702137259
Precision: 98.80%
Accuracy: 94.92%
Recall: 82.33%
F1 score: 89.80%

	2. SVC with Countvectorizer
[0.95918367 0.96258503 0.9739229  0.9569161  0.96254257]
[0.9638009  0.98148148 0.97807018 0.95111111 0.94805195]
[0.88381743 0.87966805 0.9253112  0.8879668  0.9125    ]
[0.92207792 0.92778993 0.95095949 0.91845494 0.92993631]
0.9630300550034618
0.9645031242121025
0.8978526970954357
0.9298437172120261
Precision: 96.45%
Accuracy: 96.30%
Recall: 89.79%
F1 score: 92.98%



(d). (c)+Removing To:,From:,and Date: fields of emails with above changes.
(email fields)
.


	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.95124717 0.95804989 0.94897959 0.95804989 0.94324631]
[0.97129187 0.98564593 0.97560976 0.99033816 0.97029703]
[0.84583333 0.85833333 0.83333333 0.85416667 0.81666667]
[0.90423163 0.91759465 0.8988764  0.91722595 0.88687783]
0.9519145683244922
0.9786365498189603
0.8416666666666666
0.9049612927910573
Precision: 97.86%
Accuracy: 95.19%
Recall: 84.17%
F1 score: 90.50%


	2. SVC with Countvectorizer
[0.96485261 0.96598639 0.9569161  0.95464853 0.94778661]
[0.94893617 0.96902655 0.97235023 0.96774194 0.93362832]
[0.9214876  0.90495868 0.86831276 0.86419753 0.87190083]
[0.93501048 0.93589744 0.9173913  0.91304348 0.9017094 ]
0.9580380468494625
0.958336640673604
0.8861714791007721
0.9206104204791654
Precision: 95.83%
Accuracy: 95.80%
Recall: 88.62%
F1 score: 92.06%


(e). (d)+Removing stop words, stemming and lemmatization the data set.
	

	1. Using Multinomial NaiveBayes as the Model with CountVectorizer
[0.93877551 0.93424036 0.94444444 0.9478458  0.93870602]
[0.9744898  0.98404255 0.97512438 0.98019802 0.965     ]
[0.79583333 0.77083333 0.81666667 0.825      0.80416667]
[0.87614679 0.86448598 0.88888889 0.8959276  0.87727273]
0.9408024276680024
0.9757709494042579
0.8024999999999999
0.8805443976541616
Precision: 97.58%
Accuracy: 94.08%
Recall: 80.25%
F1 score: 88.05%

	2. SVC with Countvectorizer
[0.95918367 0.97959184 0.95578231 0.95464853 0.96140749]
[0.9638009  0.97446809 0.96330275 0.93506494 0.99047619]
[0.88381743 0.95020747 0.87136929 0.89626556 0.86666667]
[0.92207792 0.96218487 0.91503268 0.91525424 0.92444444]
0.9621227681386593
0.9654225735836924
0.8936652835408022
0.9277988314997287
Precision: 96.54%
Accuracy: 96.21%
Recall: 89.37%
F1 score: 92.78%


After Applying 5-fold cross validation
![image](https://github.com/sarangics/Research/assets/65746767/a2cb3ec7-f3b1-4083-953c-2f1b4cf82409)
![image](https://github.com/sarangics/Research/assets/65746767/28da42bd-afe1-4484-a858-91b451f60d26)
Check Accuracy levels using different test cases(enrone3)

Test Cases	NB		SVC
           All					 			93.88%             96.30%
           test1=replacing only 
	special chars,numbers,whitespaces    			 94.69%	           96.05%
test2=email fields+test1          					94.85%	 95.83%
test3=stop word,lemma+test2					93.56%	95.92%
test4=stop word,stem+test2					94.24%	96.28%
test5=stop word+test2						93.63%	95.87%
test6=lemma+test2						94.76%	96.23%	
test7=stem+test2						95.28%	96.48%
test8=lemma+stem+test2					94.94%	96.24%
test9=test7-email fields					95.08%	96.46%
test10=test7+email,date,url,postal codes			95.24%	96.19%
test11=test7 +date,postal codes		   		 95.12%	96.39%
test12 =test7-email from field	(from,to)			94.99%	96.53%
test13 =test7-email from field	(from)	-replace whitespaces	95.44%	96.51%
test14= test9-replace whitespaces				95.21%	96.48%
test15=test13+remove postal codes, dates and emails		95.12%	95.94%
According to above results, test 7,9,10,11,12,13,14 and 15 have high accuracy level. Then check it with another data set.

           Check Accuracy levels using different test cases(enrone 2)

Test Cases	NB		SVC
           All					 			95.80%             97.99%
           test1=replacing only 
	special chars,numbers,whitespaces    			 97.20%	           97.87%
test2=email fields+test1          					96.84%	 97.93%
test3=stop word,lemma+test2					95.90%	97.95%
test4=stop word,stem+test2					95.88%	97.52%
test5=stop word+test2						95.65%	97.87%
test6=lemma+test2						97.01%	97.74%	
test7=stem+test2						97.48%	97.57%
test8=lemma+stem+test2					97.33%	97.65%
test9=test7-email fields					97.27%	97.99%
test10=test7+email,date,url,postal codes			97.27%	97.97%
test11=test7 +date,postal codes		   		 97.10%	97.82%
test12 =test7-email from field	(from,to)			97.23%	97.76%
test13 =test7-email from field	(from)	-replace whitespaces	97.23%	97.80%
test14= test9-replace whitespaces				97.14%	97.78%
test15=test13+remove postal codes, dates and emails		97.27%	97.67%

According to above results, test 7,8,9,10,12,13,14 and 15 have high accuracy level. Then check it with another data set.



           Check Accuracy levels using different test cases(enrone 4)

Test Cases	NB		SVC
           All					 			97.85%             97.73%
           test1=replacing only 
	special chars,numbers,whitespaces    			 97.67%	           97.81%
test2=email fields+test1          					98.00%	 97.81%
test3=stop word,lemma+test2					98.00%	97.83%
test4=stop word,stem+test2					97.85%	97.87%
test5=stop word+test2						98.04%	97.96%
test6=lemma+test2						97.98%	97.90%	
test7=stem+test2						97.58%	97.81%
test8=lemma+stem+test2					98.12%	97.52%
test9=test7-email fields					97.90%	97.54%
test10=test7+email,date,url,postal codes			97.71%	97.42%
test11=test7 +date,postal codes		   		 97.92%	97.90%
test12 =test7-email from field	(from,to)			98.06%	97.92%
test13 =test7-email from field	(from)	-replace whitespaces	97.96%	97.98%
test14= test9-replace whitespaces				97.60%	97.52%
test15=test13+remove postal codes, dates, and emails		97.56%	97.71%

According to above results, test 2,3,5,6,8,11,12, and 13 have high accuracy level. Then check it with another data set.
Check Accuracy levels using different test cases(hamnspam)

Test Cases	NB		SVC
           All					 			97.13%             97.83%
           test1=replacing only 
	special chars,numbers,whitespaces    			 98.73%	           97.70%
test2=email fields+test1          					98.57%	 97.99%
test3=stop word,lemma+test2					95.86%	97.75%
test4=stop word,stem+test2					97.99%	97.50%
test5=stop word+test2						94.47%	98.20%
test6=lemma+test2						98.40%	97.87%	
test7=stem+test2						98.65%	97.79%
test8=lemma+stem+test2					98.52%	98.36%
test9=test7-email fields					98.77%	98.32%
test10=test7+email,date,url,postal codes			98.77%	97.99%
test11=test7 +date,postal codes		   		 98.57%	98.20%
test12 =test7-email from field	(from,to)			98.77%	98.16%
test13 =test7-email from field	(from)	-replace whitespaces	98.81%	98.24%
test14= test9-replace whitespaces				98.65%	98.11%
test15=test13+remove postal codes, dates and emails		98.65%	98.32%

According to above results, test 1,2,7,9,10,11,12,13,14 and 15 have high accuracy level. Then check it with another data set.


above results shows that test13( replacing special characters numbers+ +removing stemmings+email fields(without from field)   and test12 =test7-email from field	(from,to)are include in every set of top high accuracy test cases for the four data sets.  Then considering test 12 and test 13  we can see test 13 represent highest average accuracy levels for. Both naïve base and support vector classifiers. Therefore, this cleaning method better than others, for effective spam email classification. 

Average Accuracy levels of all data sets using different test cases(enrone3,enrone2,enrone4 and hamnspam)

Test Cases	NB		SVC
           All					 			96.17%             97.46%
           test1=replacing only 
	special chars,numbers,whitespaces    			 97.07%	           97.36%
test2=email fields+test1          					97.07%	 97.39%
test3=stop word,lemma+test2					95.83%	97.36%
test4=stop word,stem+test2					96.49%	97.29%
test5=stop word+test2						95.45%	97.48%
test6=lemma+test2						97.04%	97.44%	
test7=stem+test2						97.25%	97.41%
test8=lemma+stem+test2					97.23%	97.44%
test9=test7-email fields					97.26%	97.56%
test10=test7+email,date,url,postal codes			97.25%	97.39%
test11=test7 +date,postal codes		   		 97.18%	97.58%
test12 =test7-email from field	(from,to)			97.26%	97.59%
test13 =test7-email from field	(from)	-replace whitespaces	97.36%	97.63%
test14= test9-replace whitespaces				97.15%	97.47%
test15=test13+remove postal codes, dates and emails		97.15%	97.41%



According to the above results test 13 shows highest average accuracy levels for. Both naïve base and support vector classifiers. Therefore, this cleaning method better than others, for effective spam email classification. 

Apply LSTM for spam assassin data set
. LSTM (Long short-term memory) is a deep learning method and also kind of RNN architecture that is capable of learning long-term dependencies. It is able to correlate the current information with the past information .
![image](https://github.com/sarangics/Research/assets/65746767/360a44e3-dac0-4730-ba4a-d7e0648784d7)

Apply votingclassifire() method as  an ensemble method for NB and SVM algorithms.
This technique is generally used for classification problems. In this technique, multiple models are used to make predictions for each data point. The predictions by each model are considered as a ‘vote’. The predictions which we get from the majority of the models are used as the final prediction.
![image](https://github.com/sarangics/Research/assets/65746767/bf72bade-1b18-422b-8301-451aff950d59)
Apply LSTM for Enron data sets
Enron3
Train the Model for 10 epochs. 
![image](https://github.com/sarangics/Research/assets/65746767/54570fe9-71da-42fc-ac78-b35d631e7229)
Enron4
Train the Model for 10 epochs.
![image](https://github.com/sarangics/Research/assets/65746767/0b48f479-76c8-4d37-8018-02f8d292f815)
Enron3
Train the Model for 01 epochs.
![image](https://github.com/sarangics/Research/assets/65746767/a53e65c3-1a1c-4a52-aa16-b7d52e9c16f6)
Enron4
Train the Model for 01 epochs.
![image](https://github.com/sarangics/Research/assets/65746767/078f95fb-ca34-433c-8948-ea48e01f36ed)
Combining LSTM and SVM algorithms
Accuracy 74%


































 
















