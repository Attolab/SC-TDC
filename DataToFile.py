import numpy as np

class DataToTextfile(object):
    """ This class is created to handle the data processing. Using a class for
    such a task has the advantage that we can maintain a state across multiple
    hand-overs of data chunks and the variables holding this state are visibly
    grouped together in the class. Besides, this class is written as a
    context manager by implementing __enter__ and __exit__ methods. This
    helps with automatically closing the file."""
    def __init__(self, filename):
        self.file_object = open(filename, "w")
        # write a header
        self.file_object.write(
          "{:>3} {:>3} {:>16} {:>16}\n".format(
            "#sd", "ch", "start_counter", "time"))

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print("closing file.")
        self.close()

    def close(self):
        self.file_object.close()

    def write_measurement_separator(self):
        self.file_object.write("# next measurement\n")

    def process_data(self, d):
        """ d is the same data structure as in BufDataCB4.on_data(...)
            i.e. a dictionary containing 1D arrays (and some integer values)
        """
        print("processing data chunk of length: {}".format(d["data_len"]))
        # At this point, data could be modified and filtered before
        # exporting. A thorough study of numpy's capabilities is
        # most useful.
        np.savetxt(self.file_object,
                   np.c_[d["subdevice"], d["channel"], d["start_counter"],
                         d["time"]],
                   fmt = ["%3d", "%3d", "%16d", "%16d"])
