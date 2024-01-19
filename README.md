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

Message field values:  ['<exmh-workers-admin@example.com>', 'zzzz@localhost.netnoteinc.com', 'from localhost (localhost [127.0.0.1])\tby phobos.labs.netnoteinc.com (Postfix) with ESMTP id D03E543C36\tfor <zzzz@localhost>; Thu, 22 Aug 2002 07:36:16 -0400 (EDT)', 'from phobos [127.0.0.1]\tby localhost with IMAP (fetchmail-5.9.0)\tfor zzzz@localhost (single-drop); Thu, 22 Aug 2002 12:36:16 +0100 (IST)', 'from listman.example.com (listman.example.com [66.187.233.211]) by    dogma.slashnull.org (8.11.6/8.11.6) with ESMTP id g7MBYrZ04811 for    <zzzz-exmh@example.com>; Thu, 22 Aug 2002 12:34:53 +0100', 'from listman.example.com (localhost.localdomain [127.0.0.1]) by    listman.redhat.com (Postfix) with ESMTP id 8386540858; Thu, 22 Aug 2002    07:35:02 -0400 (EDT)', 'exmh-workers@listman.example.com', 'from int-mx1.corp.example.com (int-mx1.corp.example.com    [172.16.52.254]) by listman.redhat.com (Postfix) with ESMTP id 10CF8406D7    for <exmh-workers@listman.redhat.com>; Thu, 22 Aug 2002 07:34:10 -0400    (EDT)', '(from mail@localhost) by int-mx1.corp.example.com (8.11.6/8.11.6)    id g7MBY7g11259 for exmh-workers@listman.redhat.com; Thu, 22 Aug 2002    07:34:07 -0400', 'from mx1.example.com (mx1.example.com [172.16.48.31]) by    int-mx1.corp.redhat.com (8.11.6/8.11.6) with SMTP id g7MBY7Y11255 for    <exmh-workers@redhat.com>; Thu, 22 Aug 2002 07:34:07 -0400', 'from ratree.psu.ac.th ([202.28.97.6]) by mx1.example.com    (8.11.6/8.11.6) with SMTP id g7MBIhl25223 for <exmh-workers@redhat.com>;    Thu, 22 Aug 2002 07:18:55 -0400', 'from delta.cs.mu.OZ.AU (delta.coe.psu.ac.th [172.30.0.98]) by    ratree.psu.ac.th (8.11.6/8.11.6) with ESMTP id g7MBWel29762;    Thu, 22 Aug 2002 18:32:40 +0700 (ICT)', 'from munnari.OZ.AU (localhost [127.0.0.1]) by delta.cs.mu.OZ.AU    (8.11.6/8.11.6) with ESMTP id g7MBQPW13260; Thu, 22 Aug 2002 18:26:25    +0700 (ICT)', 'Robert Elz <kre@munnari.OZ.AU>', 'Chris Garrigues <cwg-dated-1030377287.06fa6d@DeepEddy.Com>', 'exmh-workers@example.com', 'Re: New Sequences Window', '<1029945287.4797.TMDA@deepeddy.vircio.com>', '<1029945287.4797.TMDA@deepeddy.vircio.com>    <1029882468.3116.TMDA@deepeddy.vircio.com> <9627.1029933001@munnari.OZ.AU>    <1029943066.26919.TMDA@deepeddy.vircio.com>    <1029944441.398.TMDA@deepeddy.vircio.com>', '1.0', 'text/plain; charset="us-ascii"', '<13258.1030015585@munnari.OZ.AU>', 'exmh-workers@example.com', 'exmh-workers-admin@example.com', 'exmh-workers-admin@example.com', 'exmh-workers@example.com', '2.0.1', 'bulk', '<mailto:exmh-workers-request@example.com?subject=help>', '<mailto:exmh-workers@example.com>', '<https://listman.example.com/mailman/listinfo/exmh-workers>,    <mailto:exmh-workers-request@redhat.com?subject=subscribe>', 'Discussion list for EXMH developers <exmh-workers.example.com>', '<https://listman.example.com/mailman/listinfo/exmh-workers>,    <mailto:exmh-workers-request@redhat.com?subject=unsubscribe>', '<https://listman.example.com/mailman/private/exmh-workers/>', 'Thu, 22 Aug 2002 18:26:25 +0700']

 -------------------------------------- 

Message content:     Date: 

	


Data Preprocessing.
Feature Extraction
5. Extract some of main email fields. (sender, receiver and subject)
	Email from:  ['Robert Elz <kre@munnari.OZ.AU>']
	Email to:  ['Chris Garrigues <cwg-dated-1030377287.06fa6d@DeepEddy.Com>']
	Email subject:  ['Re: New Sequences Window']

6. Import all emails.
	
	['Re: New Sequences Window']
    Date:        Wed, 21 Aug 2002 10:54:46 -0500
    From:        Chris Garrigues <cwg-dated-1030377287.06fa6d@DeepEddy.Com>
    Message-ID:  <1029945287.4797.TMDA@deepeddy.vircio.com>


  | I can't reproduce this error.

For me it is very repeatable... (like every time, without fail).

This is the debug log of the pick happening ...

18:19:03 Pick_It {exec pick +inbox -list -lbrace -lbrace -subject ftp -rbrace -rbrace} {4852-4852 -sequence mercury}
18:19:03 exec pick +inbox -list -lbrace -lbrace -subject ftp -rbrace -rbrace 4852-4852 -sequence mercury
18:19:04 Ftoc_PickMsgs {{1 hit}}
18:19:04 Marking 1 hits
18:19:04 tkerror: syntax error in expression "int ...

Note, if I run the pick command by hand ...

delta$ pick +inbox -list -lbrace -lbrace -subject ftp -rbrace -rbrace  4852-4852 -sequence mercury
1 hit

That's where the "1 hit" comes from (obviously).  The version of nmh I'm
using is ...


Converting emails to plain text
	 
7. Check email content types
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

	 
	
	
	
14. Removing special characters from the data frame. And convert to lowercase letters
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



