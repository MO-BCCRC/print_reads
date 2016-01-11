'''
Created on Sep 09, 2014

@author: raniba
'''

import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    GATK RealignerTargetCreator : Create suspecious regions where a realignment will be done
    '''
    def __init__(self, component_name='print_reads', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        GATK BaseRecalibrator (Post)
        '''

        java_mem = '-Xmx3072M'
        java_jar_option = '-jar'
        print_reads_jar = self.requirements['gatk']
        print_reads_infile = self.args.infile
        print_reads_bqsr = self.args.bqsr
        print_reads_outfile = self.args.outfile
        print_reads_ref_genome = self.args.ref_genome

        cmd = self.requirements['java']
        cmd_args = [java_mem,
                    java_jar_option,
                    print_reads_jar,
                    "-T", "PrintReads",
                    "-R", print_reads_ref_genome,
                    "-BQSR", print_reads_bqsr,
                    "-I", print_reads_infile,
                    "-o", print_reads_outfile]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    print_reads = Component()
    print_reads.args = component_ui.args
    print_reads.run()

if __name__ == '__main__':

    import component_ui

    _main()
