using System;
using System.Collections.Generic;
using System.Text;

namespace AirQualityDataProcessing.Model
{
    public class UpdateInstanceRequest
    {
        public List<Instance> put { get; set; }

        public UpdateInstanceRequest()
        {
            this.put = new List<Instance>();
        }

        public void putInstance(Instance inst)
        {
            this.put.Add(inst);
        }
    }
}
