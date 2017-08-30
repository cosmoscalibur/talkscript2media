# talkscript2media

This package is an experiment to create an alternative to ARI based only in free software and open source. Convert a talk script and a set of slides to video.  

## Why?

We need a tool to automate talks video for education and other purposes. This can be possible using talk scripts and slides as source and then generate audio with TTS, join and convert to video.  
We need this because the future of resources for education is on plain text (record a video from a talk -and update this- take a lot of time).  

... but this tool exists now! Yes, its name is [ARI](https://github.com/seankross/ari) but it is depending of [Amazon Polly Service]((https://aws.amazon.com/polly/)) for TTS (you need money) and the package is not
easy to use for users not familiar with R language.   

## Goals

+   Create a tool for convert talks scripts / comments with images / slides to a video. Voice is generated using free and open TTS packages that you can install from your package management.   
+   This package will offer you a language agnostic interface that no requiered any level of knowledge in a language programming and will be easy to use for any context of talks (not only RMarkdown - R language).  
+   This package will support different file formats used in talks (maybe, using pandoc conversion).  
+   Compatibility for multiple features of ARI is important.  

## References

+   [The future of education is plain text](https://simplystatistics.org/2017/06/13/the-future-of-education-is-plain-text/).  
+   [ARI github repository](https://github.com/seankross/ari).  
+   [Read Text - Linux](https://sites.google.com/site/readtextextension/home/linux).  
	+   Festival: [bug detecting languages differents to english](https://bugs.launchpad.net/ubuntu/+source/festival/+bug/1650237). Requiere `festvox-ellpc11k` to support spanish language.   
	+   eSpeak: Recommended with MBrola voices (ex: mbrola-es2 for spanish).  
	+   SVOX Pico: You need to install `libttspico0 libttspico-utils libttspico-dat`.  
