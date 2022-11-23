# `nohcaptcha`
`nohcaptcha` is a **public** python-based [hcaptcha](https://hcaptcha.com) bypass/solver hybrid. the module first attempts to bypass hcaptcha text captchas with a list of stored answers. if the question is not saved, the module attempts to find similarities to generate an educated guess based on re-occuring stored data (**90%+ solve rate)**.

## information
nohcaptcha uses a complex system of switch the captcha mode, essentially generating easier captchas to solve. nohcaptcha uses several checks to analyze captchas and has a far better solving rate than a human. nohcaptcha also reverses hcaptcha's hsw hashing without any unnecessary browser instances.

## statistics
currently, nohcaptcha has a ``90%+`` **success rate** when solving captchas and a has consistent bypass to hcaptcha's advanced bot detection.
