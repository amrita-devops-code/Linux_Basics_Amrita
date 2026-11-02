# Linux Commands: Learn Fast

A practical learning guide for Linux command-line basics, with macOS notes where commands differ. Start with the short path below, then use the sections as a reference. You do not need to memorize everything: practise a command, inspect its output, and learn what the options change.

## Start Here: 20 Minutes

1. **Move around:** practise `pwd`, `ls -lah`, and `cd` in a practice directory.
2. **Work with files:** use `mkdir`, `touch`, `cp`, and `mv`; inspect files with `cat` or `less`.
3. **Find information:** search filenames with `find` and file contents with `grep`.
4. **Understand access:** inspect `ls -l` output and practise `chmod` on a test file.
5. **Read system state:** try `ps`, `df -h`, `free -h` (Linux), and `curl -I https://example.com`.

Commands marked **Linux only** may not be installed or behave the same on macOS. Never practise destructive commands such as `rm -r`, `chmod -R`, or disk tools on important files or systems.

## Read a Command

Most commands follow this pattern:

```text
command [options] [target]
```

For example, `ls -lah /var/log` means: run `ls`, use long and human-readable output, include hidden entries, and inspect `/var/log`. Use `man <command>` or `<command> --help` to learn options; press `q` to leave a man page. Check whether a command exists with `command -v <command>`.

## Practice Safely

Create a scratch directory and do the first exercises there:

```bash
mkdir -p ~/linux-practice
cd ~/linux-practice
pwd
touch notes.txt
printf 'first line\nERROR: practice message\n' > notes.txt
cat notes.txt
grep -n 'ERROR' notes.txt
cp notes.txt notes-copy.txt
ls -lah
```

When a command changes or deletes data, first ask: **What path will it affect? Can I preview the result?** For example, use `find ... -print` before combining `find` with deletion, and use `rm -i` when practising removal.

## Command Reference

### 1. Navigation and directory management
Mac + Linux
Used to navigate the filesystem, inspect folders, and create directories.

| Command | Purpose |
| --- | --- |
| pwd | Show current directory |
| ls | List files and folders |
| ls -l | Detailed listing |
| ls -la | Include hidden files |
| ls -lh | Human-readable sizes |
| ls -lt | Sort by modification time |
| ls -ltr | Oldest modified files first |
| cd /path | Change directory |
| cd .. | Move one level up |
| cd ~ | Go to home directory |
| cd - | Return to previous directory |
| mkdir demo | Create directory |
| mkdir -p a/b/c | Create nested directories |
| rmdir demo | Remove empty directory |
| tree | Display directory hierarchy (install if missing) |
| realpath notes.txt | Display absolute path |

Interview scenario: You SSH into a server and need to locate application configuration files. Start with pwd, ls -lah, cd, and find.
### 2. File creation and management
Mac + Linux

| Command | Purpose |
| --- | --- |
| touch file.txt | Create empty file or update timestamp |
| cat file.txt | Display file contents |
| less file.txt | Read large files |
| head -n 10 file.txt | First 10 lines |
| tail -n 10 file.txt | Last 10 lines |
| cp file.txt copy.txt | Copy file |
| cp -R dir1 dir2 | Copy directory |
| mv old.txt new.txt | Rename file |
| mv file.txt backups/ | Move file |
| rm file.txt | Delete file |
| rm -i file.txt | Confirm before deletion |
| rm -r folder | Delete directory recursively |
| file file.txt | Identify file type |
| stat file.txt | Show file metadata |
| wc -l file.txt | Count lines |
| wc -w file.txt | Count words |
| du -sh folder | Total directory size |

Caution: rm -r is destructive. Practise only on disposable folders.
### 3. File searching and text processing
Mac + Linux
Extremely important for SRE and DevOps production troubleshooting.

| Command | Purpose |
| --- | --- |
| find . -name "*.log" | Find log files |
| find . -type f | Find files |
| find . -type d | Find directories |
| find . -size +10M | Files larger than 10 MiB |
| find . -mtime -7 | Files modified within 7 days |
| grep "ERROR" logs/app.log | Search for errors |
| grep -i "error" logs/app.log | Case-insensitive search |
| grep -n "ERROR" logs/app.log | Show line numbers |
| grep -R "ERROR" logs/ | Recursive search |
| grep -v "INFO" logs/app.log | Exclude matching lines |
| grep -c "ERROR" logs/app.log | Count matching lines |
| sort file.txt | Sort lines |
| sort -u file.txt | Sort and deduplicate |
| uniq -c file.txt | Count adjacent duplicates |
| cut -d ':' -f1 file.txt | Extract first colon-separated field |
| awk '{print $1}' file.txt | Print first whitespace-separated field |
| sed 's/ERROR/WARN/g' logs/app.log | Replace text in output |
| tr 'a-z' 'A-Z' < file.txt | Convert lowercase to uppercase |
| xargs | Build command arguments from input |
| tee output.txt | Write input to file and screen |

Senior-level practice:
grep -i "error" logs/app.log | wc -l


Counts lines containing error.
awk '{print $1}' logs/app.log | sort | uniq -c


Counts occurrences of the first field, such as INFO, ERROR, and WARN.
### 4. Permissions, ownership, and security
Mac + Linux

| Command | Purpose |
| --- | --- |
| ls -l | View permissions |
| chmod 755 script.sh | Owner full access; others read/execute |
| chmod 644 file.txt | Owner read/write; others read |
| chmod 700 private_dir | Owner-only access |
| chmod +x script.sh | Make executable |
| chmod u+x script.sh | Add execute for owner |
| chmod g-w file.txt | Remove group write |
| chmod o-r file.txt | Remove others' read |
| chown user file.txt | Change owner |
| chown user:group file.txt | Change owner and group |
| chgrp group file.txt | Change group |
| umask | View default permission mask |
| id | Show user/group IDs |
| whoami | Show current username |
| sudo command | Run command with elevated privileges |
| sudo -l | List permitted sudo commands |
| getfacl file.txt | View ACLs (Linux; tool may need installation) |
| setfacl | Configure Linux ACLs |

Interview must-know: chmod 400 for private SSH keys, chmod 755 for scripts, and the difference between chmod, chown, and chgrp.
### 5. Users and groups
Mostly Linux only

| Command | Purpose |
| --- | --- |
| who | Show logged-in users |
| w | Users and their activities |
| id username | Show user identity |
| groups username | Show group memberships |
| useradd username | Create user |
| adduser username | Interactive user creation on some distros |
| usermod -aG docker username | Add user to group |
| userdel username | Delete user |
| passwd username | Change password |
| groupadd devops | Create group |
| groupdel devops | Delete group |
| su - username | Switch user |
| last | Show login history |
| getent passwd username | Query user database |
| chage -l username | Show password aging |

On macOS, who, w, id, and groups work; Linux account-management commands are different.
### 6. Process management
Mac + Linux

| Command | Purpose |
| --- | --- |
| ps | Show processes |
| ps aux | Show process details |
| ps -ef | Show all processes |
| top | Real-time process monitoring |
| pgrep -fl python | Find matching processes |
| pidof nginx | Find PID (Linux) |
| kill PID | Send SIGTERM by default |
| kill -9 PID | Force kill using SIGKILL |
| pkill processname | Signal processes by name |
| jobs | List shell jobs |
| bg | Resume job in background |
| fg | Bring job to foreground |
| nohup command & | Run detached from terminal hangup |
| nice -n 10 command | Start with adjusted priority |
| renice | Change running process priority |
| uptime | Show uptime and load averages |
| lsof -p PID | Show open files for process |
| htop | Interactive process viewer (install separately) |

Interview question: An application is consuming 100% CPU. How do you identify the responsible process and investigate it?

Start with top, ps, and lsof, then inspect application logs before deciding whether to restart anything.
### 7. CPU, memory, and system performance
Linux-focused

| Command | Purpose |
| --- | --- |
| free -h | Memory usage |
| vmstat 1 | CPU, memory, and system activity |
| iostat -xz 1 | Detailed disk I/O statistics |
| mpstat -P ALL 1 | CPU usage per core |
| sar -u 1 5 | CPU history/samples |
| sar -r | Memory statistics |
| pidstat -p PID 1 | Process resource usage |
| lscpu | CPU architecture |
| nproc | Number of available processing units |
| cat /proc/meminfo | Detailed Linux memory info |
| cat /proc/cpuinfo | Detailed CPU information |
| dmesg | Kernel ring buffer messages |
| slabtop | Kernel slab cache usage |
| pmap -x PID | Process memory mapping |
| time command | Measure execution time |

Many of these require packages such as sysstat or procps. On macOS, try top, vm_stat, sysctl -n hw.ncpu, and memory_pressure.
### 8. Disk and filesystem troubleshooting
Core commands on Mac + Linux

| Command | Purpose |
| --- | --- |
| df -h | Filesystem space usage |
| df -i | Inode usage |
| du -sh ./* | Directory sizes |
| du -ah . | Individual file/directory sizes |
| lsblk | Block devices (Linux) |
| blkid | Block device identifiers (Linux) |
| mount | Show mounted filesystems |
| umount /mountpoint | Unmount filesystem |
| findmnt | Find mounts (Linux) |
| fdisk -l | Partition information (Linux) |
| parted -l | Partition information (Linux) |
| fsck | Check/repair filesystem (caution) |
| lsof +L1 | Find open files with zero links |
| fuser -m /mountpoint | Find users of mount (Linux) |
| tune2fs -l /dev/device | ext filesystem details (Linux) |
| xfs_info /mountpoint | XFS filesystem details (Linux) |

Senior interview scenario: Disk is 100% full but deleting a log file doesn't free space. Investigate open-but-deleted files using lsof +L1.
### 9. Networking and connectivity
Some Mac + Linux; flags may differ

| Command | Purpose |
| --- | --- |
| ping -c 4 example.com | Check ICMP connectivity |
| curl -I https://example.com | Fetch HTTP headers |
| curl -v https://example.com | Debug HTTP/TLS connection |
| curl -o /dev/null -w '%{http_code}\n' https://example.com | Check HTTP status |
| dig example.com | DNS lookup |
| nslookup example.com | DNS lookup |
| host example.com | DNS lookup |
| traceroute example.com | Trace network path |
| ssh user@host | Remote login |
| ssh -i key.pem user@host | SSH using private key |
| scp file.txt user@host:/tmp/ | Secure file copy |
| sftp user@host | Secure file transfer |
| rsync -av source/ destination/ | Synchronize directories |
| nc -vz host 443 | Test TCP port |
| lsof -iTCP -sTCP:LISTEN -n -P | Show listening TCP ports |
| ifconfig | Network interfaces |
| netstat -an | Network sockets |
| arp -a | ARP cache |
| hostname | System hostname |

Linux-specific networking

| Command | Purpose |
| --- | --- |
| ip addr | Show IP addresses |
| ip link | Network interfaces |
| ip route | Routing table |
| ip neigh | Neighbor/ARP table |
| ss -tulnp | Listening TCP/UDP sockets |
| ss -s | Socket summary |
| ethtool eth0 | Network interface details |
| tcpdump -i eth0 | Capture packets |
| mtr example.com | Combined ping/traceroute |
| resolvectl status | DNS resolver status (systemd) |
| nmcli device status | NetworkManager device status |
| iptables -L -n -v | Legacy firewall rules |
| nft list ruleset | nftables firewall rules |
| ufw status | UFW firewall status |

Interview scenario: An application is unreachable on port 8080. Use ss, curl, nc, DNS checks, firewall checks, and application logs to isolate the issue.
### 10. Logs and production troubleshooting
Mostly Linux only

| Command | Purpose |
| --- | --- |
| tail -f /var/log/syslog | Follow system logs (Debian/Ubuntu where present) |
| tail -n 100 app.log | Last 100 log lines |
| grep -i "error" app.log | Find errors |
| journalctl | Read systemd journal |
| journalctl -u nginx | Nginx service logs |
| journalctl -u nginx -f | Follow service logs |
| journalctl -u nginx --since "1 hour ago" | Recent service logs |
| journalctl -p err -b | Errors from current boot |
| journalctl -k | Kernel logs |
| dmesg -T | Human-readable kernel messages |
| last -x | Login/reboot/shutdown history |
| logger "Test message" | Write syslog message |
| logrotate -d /etc/logrotate.conf | Debug log rotation |

On your Mac, practise tail -f logs/app.log, grep, awk, and less immediately.
### 11. Service management and systemd
Linux only — systemd distributions

| Command | Purpose |
| --- | --- |
| systemctl status nginx | Service status |
| systemctl start nginx | Start service |
| systemctl stop nginx | Stop service |
| systemctl restart nginx | Restart service |
| systemctl reload nginx | Reload configuration |
| systemctl enable nginx | Enable at boot |
| systemctl disable nginx | Disable at boot |
| systemctl is-active nginx | Check active state |
| systemctl is-enabled nginx | Check boot enablement |
| systemctl list-units --type=service | List loaded services |
| systemctl list-timers --all | List timers |
| systemctl daemon-reload | Reload unit definitions |
| systemd-analyze blame | Boot-time analysis |
| systemctl cat nginx | View service unit |
| systemctl show nginx | View service properties |

For interviews, understand the difference between restart, reload, enable, and start.
### 12. Archives, backups, and compression
Mac + Linux

| Command | Purpose |
| --- | --- |
| tar -cvf backup.tar configs/ | Create tar archive |
| tar -xvf backup.tar | Extract archive |
| tar -czvf backup.tar.gz configs/ | Create compressed archive |
| tar -xzvf backup.tar.gz | Extract compressed archive |
| tar -tvf backup.tar | List archive contents |
| gzip file.txt | Compress file |
| gunzip file.txt.gz | Decompress |
| zip -r backup.zip configs/ | Create ZIP |
| unzip backup.zip | Extract ZIP |
| rsync -av configs/ backups/ | Copy/synchronize |
| shasum -a 256 file.txt | SHA-256 checksum (Mac) |
| sha256sum file.txt | SHA-256 checksum (Linux) |

### 13. Shell scripting and automation
Mac + Linux

| Command/syntax | Purpose |
| --- | --- |
| echo "Hello" | Print text |
| printf '%s\n' "Hello" | Formatted output |
| read -r name | Read user input |
| export ENV=prod | Export environment variable |
| env | Show environment |
| printenv PATH | Show variable |
| source script.sh | Run script in current shell |
| bash script.sh | Run Bash script |
| bash -n script.sh | Check Bash syntax |
| bash -x script.sh | Trace script execution |
| set -e | Exit on many command failures |
| set -u | Error on unset variables |
| set -o pipefail | Pipeline fails if any component fails |
| command -v python3 | Find command |
| test -f file.txt | Test file existence |
| sleep 5 | Wait 5 seconds |
| date | Current date/time |
| date -u | UTC date/time |
| seq 1 10 | Generate number sequence |
| crontab -l | List cron jobs |
| crontab -e | Edit cron jobs |

#### Essential scripting concepts
Practise if/else, for, while, case, functions, positional arguments ($1, $2), exit codes ($?), and command substitution ($(command)).

Create a simple monitoring script:

```bash
cat > healthcheck.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

url="https://example.com"
status=$(curl -L -sS -o /dev/null -w '%{http_code}' "$url")

if [[ "$status" == "200" ]]; then
  echo "Application healthy"
else
  echo "Application returned HTTP $status"
  exit 1
fi
EOF

chmod +x healthcheck.sh
./healthcheck.sh
```

This tests HTTP response status, not full application health.
### 14. Package management
Linux only, except Homebrew

| Command | Purpose |
| --- | --- |
| apt update | Refresh package metadata (Debian/Ubuntu) |
| apt upgrade | Upgrade packages |
| apt install nginx | Install package |
| apt remove nginx | Remove package |
| apt list --installed | List installed packages |
| dpkg -l | List Debian packages |
| dpkg -S /path/file | Find owning package |
| dnf install nginx | Install on modern RHEL/Fedora |
| dnf update | Update packages |
| rpm -qa | List RPM packages |
| rpm -qf /path/file | Find owning RPM package |
| brew install wget | Install via Homebrew (Mac) |
| brew list | Installed Homebrew packages |
| brew update | Update Homebrew metadata |

### 15. Advanced Linux administration
Linux only

| Command | Purpose |
| --- | --- |
| uname -a | Kernel/system information |
| hostnamectl | Hostname/system metadata |
| timedatectl | Time and timezone |
| sysctl -a | Kernel parameters |
| sysctl -w key=value | Change runtime kernel parameter |
| ulimit -a | Shell resource limits |
| prlimit --pid PID | Process resource limits |
| strace -p PID | Trace system calls |
| strace -f -o trace.log command | Trace process and children |
| ltrace command | Trace library calls |
| perf top | CPU profiling |
| perf stat command | Performance counters |
| ldd /path/binary | Shared library dependencies |
| readelf -h /path/binary | ELF metadata |
| lsmod | Loaded kernel modules |
| modinfo module | Module details |
| sysctl vm.swappiness | View swappiness |
| swapon --show | Swap devices/files |
| getenforce | SELinux mode (where installed) |
| sestatus | SELinux status |
| aa-status | AppArmor status |
| auditctl -l | Audit rules |
| ausearch -m AVC | Search SELinux audit denials |

These are especially relevant to advanced troubleshooting interviews.
### 16. Containers and cloud-native Linux
Docker/Kubernetes CLI can run on Mac when installed and configured

| Command | Purpose |
| --- | --- |
| docker ps | Running containers |
| docker ps -a | All containers |
| docker images | Local images |
| docker logs container | Container logs |
| docker logs -f container | Follow logs |
| docker exec -it container sh | Shell into container |
| docker inspect container | Container metadata |
| docker stats | Container resources |
| docker top container | Container processes |
| docker network ls | Docker networks |
| docker volume ls | Docker volumes |
| docker system df | Docker disk usage |
| kubectl get pods -A | All Kubernetes pods |
| kubectl describe pod POD | Pod details |
| kubectl logs POD | Pod logs |
| kubectl logs POD --previous | Previous container logs |
| kubectl exec -it POD -- sh | Shell into pod |
| kubectl top pods | Pod CPU/memory |
| kubectl get events -A | Cluster events |
| kubectl get nodes -o wide | Node details |
| kubectl rollout status deployment/APP | Deployment rollout status |

These are not core Linux commands, but are essential for senior DevOps troubleshooting.
### 17. Linux storage, LVM, and containers under the hood
Linux only

| Command | Purpose |
|---|---|
| pvs | Physical volumes |
| vgs | Volume groups |
| lvs | Logical volumes |
| pvdisplay | Physical volume details |
| vgdisplay | Volume group details |
| lvdisplay | Logical volume details |
| lvextend | Extend logical volume |
| resize2fs | Resize ext filesystem |
| xfs_growfs | Grow XFS filesystem |
| `mount \| grep cgroup` | View cgroup mounts |
| cat /proc/1/cgroup | PID 1 cgroup membership |
| lsns | List namespaces |
| nsenter | Enter process namespaces |
| unshare | Create namespaces |
| systemd-cgls | Show cgroup hierarchy |
| systemd-cgtop | Cgroup resource usage |

LVM and filesystem resizing commands should be practised only in a disposable Linux VM with test volumes.

### 18. Senior DevOps interview scenarios: commands to combine
Senior interviews frequently test troubleshooting methodology rather than memorizing isolated commands.

| Scenario | First commands to consider |
| --- | --- |
| Server CPU at 100% | top, ps aux, pidstat, perf |
| Server out of memory | free -h, vmstat, dmesg, ps |
| Disk 100% full | df -h, du -sh, lsof +L1 |
| Inodes exhausted | df -i, find, du |
| Application not responding | curl, ss, systemctl, journalctl |
| DNS resolution failure | dig, resolvectl, cat /etc/resolv.conf |
| Port connection refused | ss -tulnp, nc -vz, curl -v |
| Connection timeout | ip route, ping, traceroute, tcpdump |
| SSH login fails | ssh -vvv, ls -l, journalctl -u ssh |
| Service crashes repeatedly | systemctl status, journalctl, coredumpctl |
| High disk I/O | iostat -xz, iotop, pidstat -d |
| Too many open files | ulimit -n, lsof -p, prlimit |
| Linux permissions issue | namei -l, id, ls -l, getfacl |
| Container restarting | docker logs, docker inspect, kubectl describe |
| Kubernetes pod OOMKilled | kubectl describe, kubectl logs --previous, kubectl top |
| Slow API response | curl -w, ss, top, logs |
| Server unexpectedly rebooted | last -x, journalctl -b -1, dmesg |
| Certificate/TLS problem | openssl s_client, curl -v, date |

### 19. Extra commands worth learning for senior interviews
These are often overlooked but useful in production environments.

| Command | Purpose |
| --- | --- |
| watch -n 2 'df -h' | Repeat command every 2 seconds (Linux) |
| timeout 10 command | Limit execution time (GNU/Linux) |
| flock | Prevent concurrent script runs (Linux) |
| mktemp | Create temporary file/directory |
| diff -u old.txt new.txt | Compare files |
| comm | Compare sorted files |
| split -l 1000 file.txt chunk_ | Split large file |
| paste file1 file2 | Merge lines |
| jq '.key' file.json | Parse JSON (install separately) |
| yq '.key' file.yaml | Parse YAML (install separately) |
| openssl s_client -connect example.com:443 -servername example.com | Inspect TLS connection |
| openssl x509 -in cert.pem -noout -dates | Certificate validity |
| ssh-keygen -t ed25519 | Generate SSH key |
| ssh-keygen -lf key.pub | SSH key fingerprint |
| ssh -vvv user@host | Debug SSH connection |
| namei -l /path/file | Inspect permissions along path (Linux) |
| getcap /path/binary | Linux file capabilities |
| capsh --print | Linux capability information |
| coredumpctl list | List captured crashes |
| coredumpctl info PID | Crash information |
| git diff | Review working-tree changes |
| git status | Check repository status |


## Your Hands-on Preparation Plan
You do not need to memorize every command before starting interviews. Focus on understanding command output and choosing the right tool for a production problem.
### Practice Tracker

0 / 10 completed



[ ] Navigation and files

Sections 1–2


[ ] Searching and text processing

Section 3


[ ] Permissions and users

Sections 4–5


[ ] Processes and performance

Sections 6–7


[ ] Disk and filesystems

Sections 8, 17


[ ] Networking

Section 9


[ ] Logs and systemd

Sections 10–11


[ ] Backups and shell scripting

Sections 12–13


[ ] Packages and Linux internals

Sections 14–15


[ ] Containers and troubleshooting

Sections 16, 18–19


 Copy progress checklist
### Suggested Starting Point
Start with Sections 1–4 on your MacBook, then move to processes, logs, networking, and troubleshooting. For senior-level Linux interviews, the most important skill is being able to explain why you selected a command, interpret its output, and decide your next troubleshooting step.

Once you're comfortable with the Mac-compatible commands, use an Ubuntu VM or disposable Linux environment to practise systemctl, journalctl, ss, ip, and other Linux-specific commands.

I can also take you through each section with actual terminal exercises and interview questions, checking your answers before moving to the next topic.