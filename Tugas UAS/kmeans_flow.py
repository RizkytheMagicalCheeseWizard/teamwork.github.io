from metaflow import FlowSpec, step, Parameter
class KmeansFlow(FlowSpec):
    num_docs = Parameter('num_docs', help="Number of documents", default = 1000)

    @step
    def start(self):
        import scale_data
        scale_data.load_chat(self.num_docs)
        self.next(self.end)
    
    @step
    def end(self):
        pass

if __name__ == '__dict__':
    KmeansFlow()