# The BH2k18-machine-gun #w00tw00t


The purpose of this script is just to help you gather BH2k18 talks and retrieve associated infos (description, presentations, code, ...) easily.


Aims to be a tiny script for a simple purpose.

## Examples 

The script can be used by providing a file witha list of URL (like *curated_list.txt*) :

```
./machine.py -F curated-list.txt --list-talks --resources-only                  [13:02:45]
So I became a Domain Controller
Nothing :-(
====================
Exploitation of a Modern Smartphone Baseband
Nothing :-(
====================
From Thousands of Hours to a Couple of Minutes: Automating Exploit Generation for Arbitrary Types of Kernel Vulnerabilities
slides : http://i.blackhat.com/us-18/Thu-August-9/us-18-Wu-Towards-Automating-Exploit-Generation-For-Arbitrary-Types-of-Kernel-Vulnerabilities.pdf
whitepaper : http://i.blackhat.com/us-18/Thu-August-9/us-18-Wu-Towards-Automating-Exploit-Generation-For-Arbitrary-Types-of-Kernel-Vulnerabilities-wp.pdf
source_code : Not available yet.
...
...
...
```


... or can simply query the BH json API :

```
./machine.py -F curated-list.txt --list-talks
./machine.py --list-talks                                                       [13:04:51]
11956 : Optimistic Dissatisfaction with the Status Quo: Steps We Must Take to Improve Security in Complex Landscapes
11214 : Measuring the Speed of the Red Queen's Race; Adaption and Evasion in Malware
10951 : Holding on for Tonight: Addiction in InfoSec
11073 : Finding Xori: Malware Analysis Triage with Automated Disassembly
10259 : Exposing the Bait: A Qualitative Look at the Impact of Autonomous Peer Communication to Enhance Organizational Phishing Detection
...
...
...
```


And help you to retrieve the resources associated with the talks :
```
./machine.py --list-talks -r | head                                             [13:05:39]
Optimistic Dissatisfaction with the Status Quo: Steps We Must Take to Improve Security in Complex Landscapes
slides : Not available yet.
whitepaper : Not available yet.
source_code : Not available yet.
====================
Measuring the Speed of the Red Queen's Race; Adaption and Evasion in Malware
slides : http://i.blackhat.com/us-18/Wed-August-8/us-18-Harang-Measuring-the-Speed-of-the-Red-Queens-Race.pdf
whitepaper : http://i.blackhat.com/us-18/Wed-August-8/us-18-Harang-Measuring-the-Speed-of-the-Red-Queens-Race-wp.pdf
source_code : Not available yet.
====================
...
...
...
```

