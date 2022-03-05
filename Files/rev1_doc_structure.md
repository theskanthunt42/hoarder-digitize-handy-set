# The DAP Standard

Probably something I try to define it by myself for archiving newspapers.

Yet another thoughts jumped into my mind when watching news.

## Purpose of this file format: 
I was looking for something to digitize my collections of newspaper(I am gonna to archive some newspaper down here in Peral River Delta, so only can cover some shit in China and Canton/Zhuhai/Shenzhen, but it makes sense since our great history will change by "its own" and html and pics online will faded away aSHITap but papers not) and stuff with more extendability then .cbz which adding support of more infomation about individual pages, more than just time and dates, with the ability to store some metadatas on it just like your musics with ID3 tags on it, Links to wikipedia at that very same day when this newspaper came out, where this from, who print and release it, how many pages in it, does it support ocr or sth shit like this.

Idk, if there is anyone already done it but i just dont know or whatever, anyway I am just for fun.

## How far its away to really make this work?
Well, It have to at least can be make use of not only me, but others, which requires some "at least handy" softwares to create/read this format

And it should be standarize closly sth like that with a working Python libary to work with this.

## Any ideas about this file format standard so far?
Yes. at least some but need to think closly later on

it will be looks like this:
A .DAP/dap(Stands for Digitize Archiving-purpose on newsPaper btw) file, which can based on .tar or with compression(of course why some one will use this w/o compressing it) like 7z, gzip or zip

inside a .dap it will contains a `metas.json` for saving stuff like date of publish, version of the sessions(I mean, they can re-release it, right?), the version of DAP, enabled-features stuff, colour or not, scanned by who and when... etc
and a serires images of the actual image which in PNG format(Prefer to use, but as the software you use support it, it will works), w/o size limitation
and a folder call `_META_` which contains alots of json, every single image in the root folder will have its own json, filename is the same to the images but with the file-extention of .json 
and yet another folder call `_EXT_` for extentions

Which it just a .tar/.tar.gz/.7z/.zip file laying around with something diffrent, right?

I will publish more info later.(Hope this project wont dead that quick)
