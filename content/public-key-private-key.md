Title: Public Key, Private Key
Date: 2013-04-13 09:06
Author: chris
Category: Technology
Tags: code, dsa, keygen, reference, rsa, ssh
Slug: public-key-private-key
Status: published

If you use ssh (Secure Shell) with public/private keys, here is a quick reference. The private key stays on the computer you will connect/send from. The public key goes on the computer(s) you will connect/send to. You can think of the private and public keys as a signature of the sending computer, and they are used to validate/authenticate the sender. (Keys are also affiliated with the user account that creates them.)

Create the public key, private key pair:

    ssh_keygen -t rsa

I used RSA encryption here. You can also use DSA. This generates two files: id_rsa (private key) and id_rsa.pub (public key). Move id_rsa to your .ssh directory.

    mv id_rsa ~/.ssh

Copy/send id_rsa.pub to the .ssh directory on the computer you will connect to.

    scp id_rsa.pub receiving_username@receiving_domain.com:~/.ssh

Add id_rsa.pub to the authorized_keys file on the receiving computer.

    cat id_rsa.pub >> authorized_keys

That is essentially it. Now when you connect from the computer with the private key to the computer with the public key, you will be using a secure connection.

To take this one step further and simplify connection commands, you can add an IdentityFile directive to a ssh config file. This allows you to use the keys along with a known, well used username to connect to the receiving_domain computer more quickly.

Create a config file in your .ssh directory (litterally named config) if you don't already have one. Add the reference to the private key.

    Host receiver
        User: receiving_username
        IdentityFile: ~/.ssh/id_rsa

Then, when you connect, you can issue the command

    ssh receiver

and it will ask for the pass phrase (not password) you supplied when you created the private key.

 
