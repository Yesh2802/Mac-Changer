#!/usr/bin/env python

import subprocess
import optparse
import re


def script_intro():
    print("  ......                                                                        .......")
    print("  ..,,,,...                                                                ....,,,..")
    print(" ..,:::,,...                                                         ..,,:::,,..")
    print("     ..,;ii;::,.                                                    .,,:;ii;:,..")
    print("      .,:i1t1i:,..                                              ..,:;1t1i;,..")
    print("      ..,:itff1;:,..                                         .,:;1tft1;:,.")
    print("        ..,:itffti;:,.                                    .,,;itfff1;:,.")
    print("          ..,:i1fffti;:,..                             .,,:itffft1;:,.")
    print("            ..,:;1tfLfti;:,..                       .,,;1tLLLft1;:,.")
    print("               .,:;i1tffft1;:,..                ..,:;1fLLLffti;:,.")
    print("                 .,:;i1tfLLLfti:,..          ..,:i1fLLLfft1i:,..")
    print("                   ..,:;itfLLLLfti:,..    ..,:ifLCCLfftt1;:,.")
    print("                      .,:;i1ttfffff1;:....,;tLCCCLfft1i;,..")
    print("                       ..,:i1tfffft1ii:..,;1fLLLLfft1;:,.")
    print("                       ..:;1tLLLft11ti:..,;1ttffLLft1;:,..")
    print("                       ..:;1fLLLLLft1;,..,:itffLLfff1i:,..")
    print("                        ..,;1fffLLLLLf1;;1tffLLffffti;,.")
    print("                          .,:;1fffLCGCLffLLLLfffff1;,..")
    print("                            ..:;1fLLCCCCCCLfffLf1;,..")
    print("                              .,:;1fLLLLLLLLLf1;,..")
    print("                                .,:;1fLLLLLt1;,..")
    print("                                  ..,:ittti:,.")
    print("                                     ..,,,..  ")
    print("                                      ")



def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
        parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
        (options, arguments) = parser.parse_args()
        if not options.interface:
            parser.error("[-] Please specify an interface, use --help for more info.")
        elif not options.new_mac:
            parser.error("[-] Please specify a new mac, use --help for more info")
        return options


def mac_change(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


script_intro()
options = get_arguments()
mac_change(options.interface,options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_address_search_result:
   print(mac_address_search_result.group(0))
else:
   print("[-] Could not read MAC address")