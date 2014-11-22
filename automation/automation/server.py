import logging
import multiprocessing

import util
from .consumer import Consumer
from .producer import Producer


class Server(object):
    """Server: manages shared resources, the producer, and the consumers."""

    def __init__(self, num_workers):
        self.logger = logging.getLogger('Server')
        self.db = util.init_database_client()
        self.num_workers = num_workers
        self.frame_queue = multiprocessing.JoinableQueue()
        self._setup()

    def start(self):
        self.logger.debug("Starting workers...")
        for worker in self.workers:
            worker.start()

        self.logger.debug("Discovering nodes on network.")
        self.coordinator.discover_nodes()

        self.logger.debug("Starting the producer...")
        self.producer.start()

    def shutdown(self):
        self.logger.info("Shutting down server...")
        self.producer.shutdown()
        self.logger.debug("Blocking until all consumers are done...")
        self.frame_queue.join()
        self.logger.info("All consumers have terminated.")

    def _setup(self):
        # Setup node manager.
        self.logger.debug("Initializing node manager...")
        self.manager = multiprocessing.Manager()
        self.nodes = self.manager.dict()  # discovered XBee nodes.

        # Create producer.
        self.logger.debug("Initializing producer...")
        self.producer = Producer(self.nodes, self.frame_queue)

        # Create consumers.
        self.logger.debug("Spawning consumers...")
        for i in range(self.num_workers):
            p = Consumer(args=(self.frame_queue, self.nodes, self.db))
            p.setName("Consumer {0}".format(i))
            p.daemon = True
            self.workers.append(p)
