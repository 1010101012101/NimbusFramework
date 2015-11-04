#!/usr/bin/env bash

# SERVER OPTIONS
######################################
#
# HOST
# host = localhost

# PORT
# port = 27017

# DB
# database_path = $PATH







General options:
  -h [ --help ]               show this usage information
  --version                   show version information
  -f [ --config ] arg         configuration file specifying additional options
  -v [ --verbose ] [=arg(=v)] be more verbose (include multiple times for more
                              verbosity e.g. -vvvvv)
  --quiet                     quieter output
  --port arg                  specify port number - 27017 by default
  --bind_ip arg               comma separated list of ip addresses to listen on
                              - all local ips by default
  --ipv6                      enable IPv6 support (disabled by default)
  --maxConns arg              max number of simultaneous connections - 1000000
                              by default
  --logpath arg               log file to send write to instead of stdout - has
                              to be a file, not directory
  --syslog                    log to system\'s syslog facility instead of file
                              or stdout
  --syslogFacility arg        syslog facility used for mongodb syslog message
  --logappend                 append to logpath instead of over-writing
  --logRotate arg             set the log rotation behavior (rename|reopen)
  --timeStampFormat arg       Desired format for timestamps in log messages.
                              One of ctime, iso8601-utc or iso8601-local
  --pidfilepath arg           full path to pidfile (if not set, no pidfile is
                              created)
  --keyFile arg               private key for cluster authentication
  --setParameter arg          Set a configurable parameter
  --httpinterface             enable http interface
  --clusterAuthMode arg       Authentication mode used for cluster
                              authentication. Alternatives are
                              (keyFile|sendKeyFile|sendX509|x509)
  --nounixsocket              disable listening on unix sockets
  --unixSocketPrefix arg      alternative directory for UNIX domain sockets
                              (defaults to /tmp)
  --filePermissions arg       permissions to set on UNIX domain socket file -
                              0700 by default
  --fork                      fork server process
  --auth                      run with security
  --noauth                    run without security
  --jsonp                     allow JSONP access via http (has security
                              implications)
  --rest                      turn on simple rest api
  --slowms arg (=100)         value of slow for profile and console log
  --profile arg               0=off 1=slow, 2=all
  --cpu                       periodically show cpu and iowait utilization
  --sysinfo                   print some diagnostic system information
  --noIndexBuildRetry         don't retry any index builds that were
                              interrupted by shutdown
  --noscripting               disable scripting engine
  --notablescan               do not allow table scans

Replication options:
  --oplogSize arg       size to use (in MB) for replication op log. default is
                        5% of disk space (i.e. large is good)

Master/slave options (old; use replica sets instead):
  --master              master mode
  --slave               slave mode
  --source arg          when slave: specify master as <server:port>
  --only arg            when slave: specify a single database to replicate
  --slavedelay arg      specify delay (in seconds) to be used when applying
                        master ops to slave
  --autoresync          automatically resync if slave data is stale

Replica set options:
  --replSet arg           arg is <setname>[/<optionalseedhostlist>]
  --replIndexPrefetch arg specify index prefetching behavior (if secondary)
                          [none|_id_only|all]

Sharding options:
  --configsvr           declare this is a config db of a cluster; default port
                        27019; default dir /data/configdb
  --shardsvr            declare this is a shard db of a cluster; default port
                        27018

Storage options:
  --storageEngine arg (=mmapv1) what storage engine to use
  --dbpath arg                  directory for datafiles - defaults to /data/db
  --directoryperdb              each database will be stored in a separate
                                directory
  --noprealloc                  disable data file preallocation - will often
                                hurt performance
  --nssize arg (=16)            .ns file size (in MB) for new databases
  --quota                       limits each database to a certain number of
                                files (8 default)
  --quotaFiles arg              number of files allowed per db, implies --quota
  --smallfiles                  use a smaller default file size
  --syncdelay arg (=60)         seconds between disk syncs (0=never, but not
                                recommended)
  --upgrade                     upgrade db if needed
  --repair                      run repair on all dbs
  --repairpath arg              root directory for repair files - defaults to
                                dbpath
  --journal                     enable journaling
  --nojournal                   disable journaling (journaling is on by default
                                for 64 bit)
  --journalOptions arg          journal diagnostic options
  --journalCommitInterval arg   how often to group/batch commit (ms)

WiredTiger options:
  --wiredTigerCacheSizeGB arg           maximum amount of memory to allocate
                                        for cache; defaults to 1/2 of physical
                                        RAM
  --wiredTigerStatisticsLogDelaySecs arg (=0)
                                        seconds to wait between each write to a
                                        statistics file in the dbpath; 0 means
                                        do not log statistics
  --wiredTigerJournalCompressor arg (=snappy)
                                        use a compressor for log records
                                        [none|snappy|zlib]
  --wiredTigerDirectoryForIndexes       Put indexes and data in different
                                        directories
  --wiredTigerCollectionBlockCompressor arg (=snappy)
                                        block compression algorithm for
                                        collection data [none|snappy|zlib]
  --wiredTigerIndexPrefixCompression arg (=1)
                                        use prefix compression on row-store
                                        leaf pages
