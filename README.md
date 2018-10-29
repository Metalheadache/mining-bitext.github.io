## Mining Bitext - Constructing parallel corpus from movie subtitles

This project aims to introduce a methodology for constructing aligned English-Simplified Chinese corpora from movie subtitles. Subtitles that consist of two languages usually provide viewers with alignment of sentences manually done by the author. Since the common length-based algorithm for alignment is not desirable when provided with short spoken sentences, we present a simple methodology to use statistical lexical cues to align the subtitle. This is also a viable solution for improving machine translation systems.

### Introduction

Text alignment is an important task in Natural Language Processing (NLP), it can be used to support many other NLP tasks. There are a lot of existing researches been done in the area of bilingual sentence alignment using parallel corpora \citep{Brown1991AligningCorpora}, and movie subtitle is one of the example. Movie subtitles that consist of two languages are used as parallel corpora, and a large parallel corpus with good quality has great value in the field of statistical machine translation. In addition, not only is parallel data useful for training and testing machine translation systems, many other NLP tasks have also benefited from these kinds of resource.

A typical movie subtitle file format is based on the time. They are characterized by an identifier, a time frame and a sentence. Usually, for a bilingual subtitle, text alignment is done manually by the author of the subtitle. However, since subtitle translations are not necessarily done by the same translator, directly extracting parallel corpora from movie subtitles can lead to noisy results, if we take rephrasing and different expression into consideration. In addition, different translator has different culture background and different writing habits.

### Proposed Method

For this project, we propose a simple method that consider both time frames and lexical content of the subtitles to automatically align sentence pairs. The purpose of our project is to improve the traditional method of alignment, and construct aligned parallel English-Simplified Chinese corpora from movie subtitles.

But before alignment can be applied, the subtitle corpus needs to undergo a few preprocessing steps. We will need to perform tokenization and segmentation to English and Chinese subtitles. After that, it is crucial that we select corresponding words in two languages. When it comes to individual words, in English grammar we use prefix and suffix to define different usage of a word, but in Chinese same words come with different meaning in different situations. That's when we will introduce lexical cue extension as a solution to the issue.

Previous algorithms are solely based on the time frame, which is reliable at times, but it ignores the richer information in the context. To improve alignment accuracy, we need to consider the lexical content. Anchor points are needed to be found in the context of subtitle pairs, the most relevant word pairs will be decided afterwards, ultimately alignment for a whole sentence will be completed.
