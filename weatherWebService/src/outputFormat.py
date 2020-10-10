
class OutputFormat:

    @staticmethod
    def output_format(info_origin, info_destination):
        """
            Static method that return the final format to print it in the console.
            :param info_origin: String with de weather orgin info.
            :param info_destination: String with de destination weather info.
            :return f: Final string format.
        """
        lines = '----------------------------------------------------------------------------------------------------------------------------------------'
        f = lines + '\nORIGIN:\n' + info_origin + '\nDESTINATION:\n' + info_destination
        return f